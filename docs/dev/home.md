# Introduccion para desarrollo

Esta seccion explica como trabajar con el codigo del framework GwaIO para desarrollar el pipeline de proyectos mediante plugins y extensiones o conexiones con otros DCCs. A lo largo de la documentación encontraremos recursos y ejemplos para comprender mejor la API y Framework de GwaIO.


# Requisitos

- Python 3.10+ instalado y en el `PATH`.
- GwaIO instalado y configurado para tu proyecto (desde el instalador oficial).
- Conocer virtual environments (`python -m venv`) y pip editable (`pip install -e`).
- Acceso al directorio de instalacion: `%LOCALAPPDATA%\\Programs\\GwaIO\\dev`.

# Hardware y sistema operativo

- Hardware: sin requisitos especiales.
- Sistema operativo: Windows 10 64-bit (version 21H2 o superior).

# Recursos

En la sección **DEV** de la documentación aprenderás a:

- **Desarrollar un plugin** que conecte el pipeline de tu proyecto con GwaIO.
- **Implementar el sistema de publishing** para automatizar la publicación de assets y metadatos.
- **Crear integraciones DCC** que conecten tus aplicaciones 3D/2D favoritas con GwaIO, automaticen la distribución de código e incrusten datos contextuales en tus scripts.

# Buenas practicas

- Versionar tus cambios (git) antes de reinstalar el paquete en editable.
- Mantener plantillas y configuracion sincronizadas con la documentacion.
- Seguir una convencion logica entre proyectos para reutilizar estructuras y codigos
