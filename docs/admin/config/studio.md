# Configurar el Studio

La ficha de **Studio** concentra la configuración global del estudio: nombre, URLs de instaladores de GwaIO, rutas de workspaces compartidos y ajustes comunes a todos los proyectos. Solo los roles `admin` y `local_admin` pueden editarla desde `/api/v1/studio/edit`.

## Campos disponibles
- **Name**: nombre del estudio que verá el usuario en el dashboard y en la barra lateral.
- **Windows/macOS/Linux build URL**: enlaces públicos a los instaladores de GwaIO. Se muestran en el dashboard como “Available builds” y permiten guiar a los usuarios en actualizaciones.
- **Workspace code location** (`JSON`): JSON con las rutas raíz de los workspaces del estudio, donde se alojan herramientas, scripts y recursos comunes (si aplica). Admite listas, por ejemplo:

```json
["//srv/studio/workspace", "C:/GwaIO/workspace"]
```

- **Studio configuration** (`JSON`): JSON libre con ajustes compartidos por todos los proyectos (por ejemplo, rutas de librerías, flags de features o credenciales de servicios internos). El editor incluye un visor y validador de JSON para evitar errores de formato.

## Metadatos y campos de solo lectura
- **Invite**: código de invitación que se usa en el endpoint público de alta de usuarios (`/api/v1/user`). No se edita desde la UI.
- **License expires** y **Max users**: visibles para referencia.

## Buenas prácticas
- Valida siempre el JSON con el botón “Edit JSON”; el backend rechazará campos mal formateados.
- Usa URLs HTTPS accesibles desde las máquinas cliente para los builds; enlaces locales o de LAN no funcionarán para usuarios remotos.
- Mantén la configuración de estudio lo más genérica posible y delega ajustes específicos en la configuración de cada proyecto.
