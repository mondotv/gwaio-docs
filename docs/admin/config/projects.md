# Gestión de proyectos

Los proyectos definen qué plugin carga el launcher de GwaIO, qué workspace usa y qué configuración heredan las herramientas del pipeline.

## Crear un proyecto
1. Haz clic en **New Project** en la tabla.
2. Completa los campos:
   - **Name** (obligatorio): etiqueta del proyecto que verán los usuarios.
   - **Config** (`JSON`): configuración que consume el plugin del proyecto (por ejemplo, `uuid`, rutas de publicación, convenciones de nombre, flags de pipeline). Ejemplo mínimo:

```json
{
  "uuid": "0e5c2d3b-1f0a-4b1e-a2b5-123456789abc",
  "render_farm_root": "\\\\nas\\render",
  "ocio_file": "\\\\nas\\config\\studio.ocio"
}
```

   - **Tools** (`JSON`): configuración específica de toolbars o utilidades adicionales que requiera el proyecto.
   - **Workspace code location** (`JSON`): rutas raíz del workspace del proyecto, donde se alojan herramientas, scripts y recursos propios (si aplica). Admite listas, por ejemplo:

```json
["//nas/projects/PRJ01", "D:/projects/PRJ01"]
```

3. Guarda. Si el JSON es inválido, el formulario marcará el campo en rojo; corrige y vuelve a guardar.

## Editar un proyecto existente
- Desde la tabla pulsa **Edit** en la fila correspondiente. Podrás modificar `name`, `config`, `tools` y `location`.
- El panel muestra mensajes de éxito o errores de validación (por ejemplo, JSON mal formateado o claves duplicadas).

## Recomendaciones
- Incluye siempre el `uuid` del proyecto dentro de `config` para alinear el launcher con el plugin correcto.
- Estandariza la estructura de `tools` y `config` según tus plugins para evitar divergencias entre proyectos.
