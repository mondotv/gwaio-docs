#!/usr/bin/env python3
"""
gen_code_docs.py — Generate documentation for each script package in docs/dev and docs/dev/internal
based on docs/.nav.yml.
  - Read docs/.nav.yml to process:
    * "Dev Guide": only entries with sub-items (lists), to extract public script packages
    * "Dev Guide Internal": similar to extract private script packages
  - For each detected package:
    * Copy static .md files from <src_root>/docs (skip examples and tests)
    * Generate .md per .py with ::: mkdocstrings (skip __init__.py, examples and tests)
    * modules.md index removed for simplicity
"""
import argparse
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
    level = logging.DEBUG if debug else logging.WARNING
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_nav() -> dict:
    with open(NAV_YML, encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_ignore(path: Path, ignore_list: list[str]) -> bool:
    normalized = [entry.strip("/\\") for entry in ignore_list]
    return any(part in normalized for part in path.parts)


# Extract packages from a section, considering only items with sub-lists.
# Look for paths under 'dev/...'
def extract_plugins(section, label: str):
    plugins = set()

    def recurse(items):
        for item in items:
            if isinstance(item, dict):
                for val in item.values():
                    if isinstance(val, list):
                        recurse(val)
            elif isinstance(item, str) and item.startswith('dev/'):
                parts = Path(item).parts
                plugins.add((parts, False))
                logger.debug("Found public script package %s in %s", parts[1], label)
            elif isinstance(item, str) and item.startswith('dev_internal/'):
                parts = Path(item).parts
                plugins.add((parts, True))
                logger.debug("Found internal script package %s in %s", parts[1], label)

    recurse(section)
    return {parts[1]: is_int for parts, is_int in plugins}


def is_newer(src: Path, dst: Path) -> bool:
    return src.is_file() and (not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime)


def generate_code_docs(nav: dict, ignore_list: list[str]) -> bool:
    public_section = next((entry['Dev Guide'] for entry in nav['nav'] if isinstance(entry, dict) and 'Dev Guide' in entry), [])
    internal_section = next((entry['Dev Guide Internal'] for entry in nav['nav'] if isinstance(entry, dict) and 'Dev Guide Internal' in entry), [])

    # Build package maps
    pub_map = extract_plugins(public_section, "Dev Guide")
    int_map = extract_plugins(internal_section, "Dev Guide Internal")
    logger.debug("Public script packages: %s", list(pub_map.keys()))
    logger.debug("Internal script packages: %s", list(int_map.keys()))

    # Build list of packages with paths (avoid duplicates)
    codes = []
    for name, _ in pub_map.items():
        src_root = GWAIO_ROOT / name
        dest_base = DEST_PUBLIC_ROOT / name
        codes.append({'name': name, 'src_root': src_root, 'dest_base': dest_base})

    for name, _ in int_map.items():
        src_root = GWAIO_ROOT / name
        dest_base = DEST_INTERNAL_ROOT / name
        codes.append({'name': name, 'src_root': src_root, 'dest_base': dest_base})

    changed = False
    for code in codes:
        src_root = code['src_root']
        dest_base = code['dest_base']
        logger.debug("Processing script package %s: %s -> %s", code['name'], src_root, dest_base)
        dest_base.mkdir(parents=True, exist_ok=True)

        # Copy static MD from <src_root>/docs, skipping 'examples' and 'tests'
        docs_src = src_root / 'docs'
        if docs_src.exists():
            logger.debug("Scanning static docs in %s", docs_src)
            for src in docs_src.rglob('*.md'):
                if is_ignore(src, ignore_list):
                    logger.debug("Skipping due to ignore %s", src)
                    continue
                rel = src.relative_to(docs_src)
                dst = dest_base / rel
                if is_newer(src, dst):
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
                    logger.debug("Copied %s -> %s", src, dst)
                    changed = True
                else:
                    logger.debug("No changes in %s", dst)
        else:
            logger.debug("Script package %s has no docs folder", code['name'])

        # Generate MD for .py modules, skipping __init__.py, examples and tests
        for py in src_root.rglob('*.py'):
            if 'docs' in py.parts or py.name == '__init__.py' or is_ignore(py, ignore_list):
                logger.debug("Skipping python file %s", py)
                continue
            rel = py.relative_to(Path(src_root).parent).with_suffix('')
            md_path = dest_base.joinpath(*rel.parts).with_suffix('.md')
            if is_newer(py, md_path):
                md_path.parent.mkdir(parents=True, exist_ok=True)
                long_module_name = {'.'.join(rel.parts)}
                md_path.write_text(f"# `{long_module_name}`\n\n::: {long_module_name}\n", encoding="utf-8")
                logger.debug("Generated module stub %s", md_path)
                changed = True
            else:
                logger.debug("Stub unchanged for %s", md_path)

    return changed



def main() -> None:
    # configure_logging(args.debug)
    # configure_logging(True)
    logger.debug("Repo root: %s", REPO_ROOT)
    nav = load_nav()
    ignore_list = nav.get("ignore", [])
    logger.debug("Nav file loaded from %s", NAV_YML)
    logger.debug("Ignored entries: %s", ignore_list)
    changed = generate_code_docs(nav, ignore_list)
    print("Script docs updated in docs/dev" if changed else "No changes in script docs")


main()