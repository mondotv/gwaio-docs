# Introduccion al Publisher Framework

Guia practica para crear un pipeline de publicación con procesos personalizados de colección, validación, extracción y envío de datos. Incluye la definición de tareas, checks y push, además de una interfaz para ejecutar la secuencia.

## Contenidos
- Tareas de colección: `CollectTask`, `CollectPreview`, `CollectFile`, `CollectBID`, `CollectDescription`.
- Validaciones: `CheckRepeatedNameNodes`, `CheckPastedNodes`, `CheckUnknownNodes`.
- Extracción: `ExtractModel`.
- Push: `PushSGModel`.

## Requisitos
Instala PySide6 o PySide2 y dependencias necesarias:
```bash
pip install PySide6
# o
pip install PySide2
```

## Prerrequisitos
- Python con PySide2/PySide6 y entorno compatible.
- Familiaridad con la API de Python de Maya si implementas checks sobre nodos de Maya.

## 1. Imports y logging
```python
from pathlib import Path
import logging
try:
    from PySide6.QtWidgets import QApplication
except:
    from PySide2.QtWidgets import QApplication

from publisher.core import Collect, Check, Extract, Push, Manager
from publisher.ui.widget import ManagerWidget

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

## 2. Clases Collect
```python
class CollectTask(Collect):
    name = "task_id"
    collect_type = int
    def process(self, context):
        self.value = 512

class CollectPreview(Collect):
    name = "preview"
    collect_type = Path
    def process(self, context):
        self.value = Path("/test_folder/preview.jpg")
```

- `CollectTask` recoge un ID de tarea (entero).
- `CollectPreview` recoge la ruta de una imagen de previsualización.

## 3. Clases Check
Validan los datos recolectados. Ejemplo (Maya) para nodos duplicados:
```python
class CheckRepeatedNameNodes(Check):
    name = "Check repeated node names"
    info = "Checks whether there are 2 or more nodes sharing the same short name."

    def process(self, context):
        import maya.cmds as cmds
        status = True
        errors = []
        all_dag_list_long = cmds.ls(type="transform", l=True)
        all_dag_list_short = [item.split("|")[-1] for item in all_dag_list_long]
        if len(all_dag_list_short) != len(set(all_dag_list_short)):
            repeated_nodes = [
                node for node in all_dag_list_long
                if all_dag_list_short.count(node.split("|")[-1]) > 1
            ]
            errors = [{"text": "Repeated node names", "list": [[node, node] for node in repeated_nodes]}]
            status = False
        return status, errors
```

## 4. Clases Extract y Push
```python
class ExtractModel(Extract):
    name = "Extract USD"
    def process(self, context):
        file = context.get_data("file")
        logger.debug(f"THIS IS FILE: {file}")

class PushSGModel(Push):
    name = "Push Version"
    def process(self, context):
        ...
```

- `ExtractModel` actúa sobre el archivo recolectado.
- `PushSGModel` enviaría la versión generada.

## 5. Crear y ejecutar el Manager
```python
def main() -> None:
    app = QApplication()
    manager = Manager()

    manager.register(CollectTask)
    manager.register(CollectFile)
    manager.register(CollectPreview)
    manager.register(CollectBID)
    manager.register(CollectDescription)
    manager.register(CheckRepeatedNameNodes)
    manager.register(CheckPastedNodes)
    manager.register(CheckUnknownNodes)
    manager.register(ExtractModel)
    manager.register(PushSGModel)

    interface = ManagerWidget(manager)
    interface.show()
    try:
        app.exec()
    except:
        app.exec_()

if __name__ == "__main__":
    main()
```

- Registra todos los procesos en el `manager` y muestra la interfaz de `ManagerWidget`.

## Ejecutar la aplicación
```bash
python your_script_name.py
```
Verás una interfaz con los procesos registrados para ejecutarlos en secuencia, revisar resultados y manejar errores.

## Conclusión
Ejemplo básico de recolección, validación y publicación. Puedes ampliar funcionalidad añadiendo nuevas clases `Collect`, `Check`, `Extract` o `Push` según tus casos de uso.
