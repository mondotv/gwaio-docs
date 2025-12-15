#!/usr/bin/env python3
"""
code_to_md.py — Genera documentación Markdown por módulo, función, clase y método.

Basado en la lógica de gen_addon_docs:
- Lee docs/.nav.yml para obtener los paquetes públicos (Dev Guide) e internos (Dev Guide Internal).
- Para cada archivo .py (excluye __init__.py, docs y rutas ignoradas):
  * Crea una carpeta con el nombre del módulo y genera un index.md que apunta al módulo completo.
  * Crea un .md por cada función toplevel.
  * Crea una carpeta por clase con su propio index.md (no genera métodos).
"""
import argparse
import ast
import logging
from pathlib import Path

import yaml

# Settings
REPO_ROOT = Path(__file__).parent.parent.resolve()
GWAIO_ROOT = Path(__file__).parent.parent.parent.resolve()
NAV_YML = REPO_ROOT / "docs" / ".nav.yml"
DEST_PUBLIC_ROOT = REPO_ROOT / "docs" / "dev"
DEST_INTERNAL_ROOT = REPO_ROOT / "docs" / "dev_internal"
logger = logging.getLogger(__name__)


def configure_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_nav() -> dict:
    with open(NAV_YML, encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_ignore(path: Path, ignore_list: list[str]) -> bool:
    normalized = [entry.strip("/\\") for entry in ignore_list]
    return any(part in normalized for part in path.parts)


def extract_packages(section, label: str):
    packages = set()

    def recurse(items):
        for item in items:
            if isinstance(item, dict):
                for val in item.values():
                    if isinstance(val, list):
                        recurse(val)
            elif isinstance(item, str) and item.startswith("dev/"):
                parts = Path(item).parts
                packages.add((parts, False))
                logger.debug("Found public script package %s in %s", parts[1], label)
            elif isinstance(item, str) and item.startswith("dev_internal/"):
                parts = Path(item).parts
                packages.add((parts, True))
                logger.debug("Found internal script package %s in %s", parts[1], label)

    recurse(section)
    return {parts[1]: is_internal for parts, is_internal in packages}


def is_newer(src: Path, dst: Path) -> bool:
    return src.is_file() and (not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime)


def parse_definitions(py_file: Path):
    """Return top-level functions and classes."""
    source = py_file.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(py_file))

    functions: list[str] = []
    classes: list[str] = []

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return functions, classes


def write_md(md_path: Path, title: str, target: str) -> None:
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(f"# `{title}`\n\n::: {target}\n", encoding="utf-8")


def generate_code_docs(nav: dict, ignore_list: list[str]) -> bool:
    public_section = next((entry["Dev Guide"] for entry in nav["nav"] if isinstance(entry, dict) and "Dev Guide" in entry), [])
    internal_section = next((entry["Dev Guide Internal"] for entry in nav["nav"] if isinstance(entry, dict) and "Dev Guide Internal" in entry), [])

    pub_map = extract_packages(public_section, "Dev Guide")
    int_map = extract_packages(internal_section, "Dev Guide Internal")
    logger.debug("Public script packages: %s", list(pub_map.keys()))
    logger.debug("Internal script packages: %s", list(int_map.keys()))

    packages = []
    for name in pub_map.keys():
        packages.append({"name": name, "src_root": GWAIO_ROOT / name, "dest_base": DEST_PUBLIC_ROOT / name})
    for name in int_map.keys():
        packages.append({"name": name, "src_root": GWAIO_ROOT / name, "dest_base": DEST_INTERNAL_ROOT / name})

    changed = False
    for pkg in packages:
        src_root = pkg["src_root"]
        dest_base = pkg["dest_base"]
        logger.info("Processing script package %s", pkg["name"])
        dest_base.mkdir(parents=True, exist_ok=True)

        # Copy static Markdown docs from <src_root>/docs
        docs_src = src_root / "docs"
        if docs_src.exists():
            logger.debug("Copying static docs from %s", docs_src)
            for src in docs_src.rglob("*.md"):
                if is_ignore(src, ignore_list):
                    logger.debug("Skipping doc due to ignore %s", src)
                    continue
                rel = src.relative_to(docs_src)
                dst = dest_base / rel
                if is_newer(src, dst):
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
                    logger.debug("Copied %s -> %s", src, dst)
                    changed = True
        else:
            logger.debug("No docs folder for %s", pkg["name"])

        for py in src_root.rglob("*.py"):
            if "docs" in py.parts or py.name == "__init__.py" or is_ignore(py, ignore_list):
                logger.debug("Skipping %s", py)
                continue

            rel = py.relative_to(src_root).with_suffix("")
            module_dir = dest_base.joinpath(*rel.parts)
            module_name = ".".join((pkg["name"], *rel.parts))

            # Module index
            module_index = module_dir / "index.md"
            if is_newer(py, module_index):
                logger.debug(f"Detect changes {py} - {module_index}")
                write_md(module_index, rel.parts[-1], module_name)
                logger.debug(f"Wrote module index {module_index}", )
                changed = True

            functions, classes = parse_definitions(py)

            for func in functions:
                func_md = module_dir / f"{func}.md"
                if is_newer(py, func_md):
                    write_md(func_md, func, f"{module_name}.{func}")
                    logger.debug("Wrote function doc %s", func_md)
                    changed = True

            for cls in classes:
                cls_dir = module_dir / cls
                cls_index = cls_dir / "index.md"
                if is_newer(py, cls_index):
                    write_md(cls_index, cls, f"{module_name}.{cls}")
                    logger.debug("Wrote class index %s", cls_index)
                    changed = True

    return changed



def main() -> None:
    # configure_logging(True)
    logger.debug("Repo root: %s", REPO_ROOT)
    nav = load_nav()
    ignore_list = nav.get("ignore", [])
    logger.debug("Ignored entries: %s", ignore_list)
    changed = generate_code_docs(nav, ignore_list)
    print("Code docs updated" if changed else "No changes in code docs")


main()
