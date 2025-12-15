# Administración de usuarios

Desde **Users** puedes dar de alta cuentas para GwaIO, desactivar accesos o resetear contraseñas.

## Crear una cuenta
1. Pulsa **New User**.
2. Rellena:
   - **Username**: identificador que usa GwaIO en las peticiones.
   - **Email**: debe ser único en la base de datos.
   - **Password**: se almacena con hash al guardar.
   - **Active**: marca si la cuenta puede iniciar sesión.
3. Guarda. El usuario hereda automáticamente la fecha de expiración de licencia del estudio y queda vinculado a todos los proyectos del estudio por defecto.

## Editar un usuario
- Usa **Edit** en la tabla. Podrás cambiar `username`, `email` y el estado **Active**.
- El campo **Password** acepta un valor nuevo opcional; si lo dejas vacío se mantiene la contraseña actual.

## Roles y permisos
- Los usuarios desactivados (`is_active = false`) siguen existiendo en el histórico pero no tienen acceso a GwaIO.
