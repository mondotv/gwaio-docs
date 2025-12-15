# Task Publishing Framework

Este framework de publicación de tareas en Python está pensado para agilizar la ejecución de procesos secuenciales como recolección de archivos, validación, extracción y actualización de bases de datos. Permite registrar y ejecutar procesos personalizados dentro de una estructura flexible, usando un contexto compartido para intercambiar datos.

## Características
- **Modular**: Define y registra distintos tipos de procesos (`Collect`, `Check`, `Extract`, `Push`).
- **Contexto compartido**: Usa un objeto `Context` para compartir datos entre procesos.
- **Gestión de errores**: Rastrea y gestiona errores mediante la clase `ErrorProcess`.
- **Callbacks**: Ejecuta funciones callback al terminar los procesos.
- **Integración sencilla**: Extensible y flexible para crear procesos a medida.

## Uso básico
1. **Crear una clase de proceso personalizada**

   Para definir un proceso nuevo, hereda de alguno de los tipos abstractos (`Collect`, `Check`, `Extract`, `Push`) e implementa `process`. Ejemplo de colección:
   ```python
   from publisher.core import Collect

   class CustomCollect(Collect):
       name = "Collect Files"
       collect_type = list  # tipo esperado

       def process(self, context):
           files = ["file1.txt", "file2.txt"]
           self.value = files
   ```
2. **Registrar y ejecutar procesos**
   ```python
   from publisher.core import Manager

   manager = Manager()
   manager.register(CustomCollect)
   manager.publish()

   collected_files = manager.context.get_data("Collect Files")
   print(collected_files)  # ['file1.txt', 'file2.txt']
   ```
3. **Gestión de errores y estado**
   ```python
   from publisher.core import Process, Context

   class MyCheck(Process):
       name = "Custom Check"

       def process(self, context):
           if not context.get_data("required_data"):
               self.add_error("Missing data", "The required_data key is missing in context.")
               self.set_status(False)

   check = MyCheck(manager)
   manager.register(check)
   manager.publish()
   ```
4. **Callbacks**
   ```python
   def notify_user(process):
       print(f"Process {process.name} has finished!")

   check.add_callback(notify_user)
   ```

## Estructura del proyecto
- `core.py`: Clases base (`Process`, `Collect`, `Check`, `Extract`, `Push`) y `Manager`.
- `tests/`: Pruebas.
- `examples/`: Ejemplos prácticos de un publisher sencillo.
- `docs/`: Documentación con Sphinx.

## Extensibilidad
El framework es extensible: puedes crear nuevos procesos heredando de `Process` y adaptarlos. Ejemplo de extracción:
```python
from publisher.core import Extract

class CustomExtract(Extract):
    name = "Extract Data"

    def process(self, context):
        data = context.get_data("collected_files")
        extracted_data = [file.upper() for file in data]
        self.context.set_data("extracted_data", extracted_data)
```
