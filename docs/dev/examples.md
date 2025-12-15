Para desarrollar un pipeline con GwaIO, usamos el framework de GwaIO, que nos automatiza la creacion de una estructura ordenada en la que podremos trabajar y desarrollar a distintos niveles mediante los workspaces.

La filosofia del framework de GwaIO es poder tener un workspace generico para todos los proyectos, esto interesa cuando queres hacer una configuracion de pipeline global como base para todos los proyectos del estudio.

## Estructura del workspace

- **`widgets`**: recursos de interfaz. Dentro encontraras ejemplos de widgets que se pueden utilizar en GwaIO, la idea de esta carpeta es agrupar los widgets genéricos.
- **`plugins`**: Esta carpeta debe contener los plugins de pipeline desarrollados, estos se cargarán automaticamente en GwaIO cuando setees la carpeta de workspace en el panel de adiminstracion del estudio o de algun proyecto.
  - `plugin_example.py`: plugin de ejemplo.
- **`utilities/<dcc>`**: utilidades específicas por DCC (Maya, Nuke, Houdini, Blender, Photoshop, Painter, Deadline).
  - Incluyen `__init__.py`, carpetas `modules`, `plug-ins`, `tools`, y `scripts/userSetup.py` (Maya).
- **`docs/README.md`**: documentación base que acompaña al proyecto generado.

## 1. Creamos el workspace del estudio (Opcional)

Crear un workspace genérico es recomendable para compartir configuración entre proyectos. Ubícalo en una ruta accesible para todo el estudio (p.ej. `C:/DemoStudio/generic`). Sigue la [Guía de Setup](../../dev/setup).

## 2. Registrar el workspace de estudio (opcional)
Registra la ruta en el panel de administración del estudio para que GwaIO lo detecte. Campo `Workspace code location` (ejemplo):
```json
["C:/DemoStudio/generic"]
```
Campos de referencia: [Studio Fields](../../admin/config/studio/#campos-disponibles).

## 3. Crear proyectos
Crea el proyecto en el panel de administración para configurar reglas de pipeline. Referencia: [Crear nuevo proyecto](../../admin/config/projects).

## 4. Workspace del proyecto
Crea el workspace específico del proyecto en una ruta accesible (ej. `C:/DemoStudio/DemoProject`). Sigue la [Guía de Setup](../../dev/setup).

## 5. Registrar el workspace del proyecto
Añade la ruta en el panel del proyecto (`Workspace code location`):
```json
["C:/DemoStudio/DemoProject"]
```
Campos de referencia: [Project Fields](../../admin/config/studio/#campos-disponibles).

## 6. Desarrollo de plugins
Los plugins encapsulan reglas de pipeline y pueden heredar de otros plugins para reutilizar lógica de estudio en proyectos. Esto permite aplicar cambios globales, pero exige cautela para no propagar errores masivamente.

![](../../assets/diagrams/plugin_workflow.drawio)

!!! Info
    Los plugins de proyecto deben incluir `PROJECT_UUID` para ser visibles en GwaIO. Los plugins genéricos sirven de base y no se listan directamente.

### 6.1 Plugin genérico

```python
# C:/DemoStudio/generic/plugins/demo_studio_project.py
from logging import getLogger

from gwaio.task_schema.plugins.shotgrid_plugin import ShotgridPlugin
from widgets.qt_classes.toolbar_example import ShellToolbar

logger = getLogger(__name__)

class DemoStudioPlugin(ShotgridPlugin):
    SHOTGRID_URL = "https://<studio>.shotgunstudio.com" # edit url

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._toolbars += [[ShellToolbar, "Shell Studio Toolbar"]]

```

### 6.2 Plugin de proyecto

=== "Heredado del estudio"
    
    ```python
    # C:/DemoStudio/DemoProject/plugins/demo_studio_project.py
    from logging import getLogger

    from plugins.demo_studio_plugin import DemoStudioPlugin
    from widgets.qt_classes.toolbar_example import ShellToolbar

    logger = getLogger(__name__)

    class DemoProjectPlugin(DemoStudioPlugin):
        SG_PROJECT_ID = 551
        PROJECT_UUID = "c5969a17-c0a1-44bc-88a2-cb3537e5d1d4" # edit UUID
        title = "Demo Plugin Example"
        project_shortname = "ple"
        env_name = "PLUGINEXAMPLE"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._toolbars += [[ShellToolbar, "Shell Project Toolbar"]]
    ```

=== "Sin heredar del estudio"

    ```python
    # C:/DemoStudio/DemoProject/plugins/demo_studio_project.py
    from logging import getLogger

    from gwaio.task_schema.plugins.maya_3d_plugin import Maya3DPlugin
    from widgets.qt_classes.toolbar_example import ShellToolbar

    logger = getLogger(__name__)

    class DemoProjectPlugin(ShotgridPlugin):
        SG_PROJECT_ID = 551
        SHOTGRID_URL = "https://<studio>.shotgunstudio.com" # edit url
        PROJECT_UUID = "c5969a17-c0a1-44bc-88a2-cb3537e5d1d4" # edit UUID
        title = "Demo Plugin Example"
        project_shortname = "ple"
        env_name = "PLUGINEXAMPLE"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._toolbars += [[ShellToolbar, "Shell Project Toolbar"]]

    ```

!!! Warning
    Mantén control de versiones y revisa los cambios antes de propagar plugins heredados para evitar introducir errores en todos los proyectos.
