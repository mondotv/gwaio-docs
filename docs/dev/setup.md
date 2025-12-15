# GwaIO Framework

Para desarrollar el pipeline con GwaIO, se distribuye con la instalación un Framework que permite ser el andamiaje de proyectos, plantillas y herramientas. A continuación se explica como instalar el framework en una estacion de trabajo y como generar una nueva estructura de proyecto "base".

Cuando GwaIO se instala mediante el instalador oficial, el codigo del framework queda en:

```
%LOCALAPPDATA%\Programs\GwaIO\dev
```

## Requisitos previos

1. **Python 3.10+** instalado y agregado al `PATH` del sistema.
2. Permisos para instalar paquetes de Python para el usuario actual o dentro de un entorno virtual.

## Instalación

La recomendacion es trabajar dentro de un entorno virtual para mantener las herramientas aisladas de otros proyectos.

1. Abre **Command Prompt** (cmd.exe) y cambia a tu directorio de trabajo preferido.
2. (Opcional) crea y activa un entorno virtual:
        ```cmd
        py -3.10 -m venv .venv
        .venv\Scripts\activate
        ```
3. Instala el framework: Usa el modo dinámico se quieres que el framework se actualice cuando actualices GwaIO, por el contrario utiliza el modo estático.
    1. En modo dinámico:

        === "CMD"

            ```cmd
            pip install -e "%LOCALAPPDATA%/Programs/GwaIO/dev"
            ```

        === "Poweshell"

            ```cmd
            pip install -e "$env:LOCALAPPDATA/Programs/GwaIO/dev"
            ```

    2. En modo estático:

        === "CMD"

            ```cmd
            pip install "%LOCALAPPDATA%/Programs/GwaIO/dev"
            ```

        === "Poweshell"

            ```cmd
            pip install "$env:LOCALAPPDATA/Programs/GwaIO/dev"
            ```

## Crear la estructura base del proyecto

1. Elige un directorio destino donde quedara la carpeta del nuevo proyecto. La CLI creara un subdirectorio con el nombre proporcionado en `--name`.
2. Ejecuta el comando (Ejemplo):
        ```cmd
        gwaio setup --name StudioPipeline --path D:/Studio/Generic/
        ```

## Desinstalación

Para quitar el framework del entorno actual:

```cmd
pip uninstall gwaio
```

Si creaste un entorno virtual dedicado, simplemente elimina el directorio `.venv`.
