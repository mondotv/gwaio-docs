# Manual de usuario de GwaIO
Última actualización: 2022/Nov/21  
Autores: Emanuel Aguado Pérez, Juan Moraga Marín

## ¿Qué es GwaIO?
GwaIO es una herramienta que permite a sus usuarios conectar su estación de trabajo con el servidor compartido de la empresa y con la base de datos que se use para el proyecto. 

A nivel práctico, GwaIO es una aplicación que permite a los artistas ver una lista de tareas sobre las que tiene que trabajar. Además, permite fácilmente generar ficheros nuevos automatizando la nomenclatura de éstos, la recogida el input de tareas anteriores, la publicación en la base de datos de nuevas versiones etc.

## Requisitos mínimos del sistema 
Para ejecutar y utilizar GwaIO, su equipo debe cumplir con las especificaciones técnicas mínimas que se indican a continuación.  
Windows 10 de 64 bits (versión 21H2) o posterior

## Requisitos adicionales del sistema
GwaIO integra dentro de sus funcionalidades otros programas, los cuales amplían el abanico de herramientas disponibles, aunque éstos no sean necesarios, es recomendable disponer de ellos: 
* [RV](https://www.shotgridsoftware.com/rv/download/)
* [FFmpeg](https://ffmpeg.org/)

Además, si se quiere utilizar el sistema de sincronización que viene incluido con GwaIO, se deberá tener montado el recurso compartido que se utilice como carpeta raíz del proyecto. En Windows no será necesario ya que se utilizan rutas UNC, pero en Mac y Linux se debe montar el recurso raíz como disco SMB.  
En el caso de que el ordenador esté en remoto, se deberá acceder a la red a través de una VPN.

## Primeros pasos
Cuando inicias GwaIO por primera vez, eres presentado con la siguiente interfaz:  
![Logged out state](img/logged-out-general-interface.png "Logged out state")   
Como es natural, no tiene ningún dato cargado todavía, ya que para poder ver datos tienes que identificarte primero en la app.

### Panel de Login 
Cuando inicias GwaIO por primera vez, no tendrás una cuenta vinculada. Para ello tienes que loguearte con la cuenta que te proporcione tu IT.  Primero tenemos que acceder al “Panel de Login”. Este panel se encuentra en la región inferior izquierda de la aplicación: 

Escriba las credenciales de usuario y contraseña para iniciar sesión. Para finalizar presione el botón aceptar. 

Una vez logueado, el estatus pasará de “not logged” a “logged”.

![Logged out state](img/logging-dock.png "Logged out state")

## Inicialización del proyecto 

Una vez identificado en la aplicación, ya se puede tener acceso a los proyectos instalados en GwaIO. Para cargar un proyecto, haga clic en el menú desplegable llamado “Menú de Plugins”, el cual se encuentra en la barra de menús del programa, en la parte superior de la ventana. Haga clic en el plugin del proyecto que desea cargar. 

![Load plugin](img/plugins-load-plugin.png "Load plugin")

Cuando se inicializa un proyecto, el programa carga el plugin vinculado a este proyecto y a continuación carga automáticamente tanto las tareas del proyecto en el “Panel de Tareas”, como las barras de herramientas asociadas al mismo. 

## Espacio de trabajo 

La interfaz de usuario se divide en dos paneles principales, el “Panel de Tareas” y el “Panel de Ficheros”. Tiene además una “Barra de Menús” y una “Barra de Estatus”. 

![Workspace](img/workspace-general-interface.png "Workspace")

Adicionalmente tiene otros paneles y barras de herramientas secundarias que se pueden solapar entre sí, desacoplar de la ventana principal y reacoplar de nuevo, dando la posibilidad de customizar el espacio de trabajo. A continuación, vamos a verlos uno a uno. 

## Paneles principales 

### Panel de Tareas 

El “Panel de Tareas” muestra la información relativa a las tareas creadas para cada proyecto. 

Esta información se muestra en forma de tabla, donde cada tarea es una fila y cada columna son los datos con los que se puede filtrar en el “Panel de Filtros” 

Las teclas de control y shift funcionan igual que en el explorador de windows y permite seleccionar varias tareas.  

![Panel task](img/panel-task-general-interface.png "Panel task")


### Panel de Ficheros 

El “Panel de Ficheros” muestra los ficheros existentes para la tarea seleccionada en el “Panel de Tareas”. Si no hay ninguna tarea seleccionada, este menú se muestra vació. A continuación, se muestran dos imágenes, la primera con ninguna tarea seleccionada y la segunda con una tarea seleccionada. Si se seleccionan varias tareas, el “Panel de Ficheros” muestra la última tarea seleccionada. 

![Unselected panel task](img/panel-task-item-unselected.png "Unselected panel task")  

![Workspace](img/panel-task-item-selected.png "Workspace")


Adicionalmente el “Panel de Ficheros” tiene una barra de navegación y un botón para subir a la carpeta continente de la carpeta que se muestra actualmente. 

![Panel task with selected task](img/panel-files-path-editor.png "Panel task with selected task")


Si se pone una dirección válida y se pulsa la tecla “Enter”, el “Panel de Ficheros” se actualiza a la ruta escrita. 

Además, tiene funcionalidades similares a la de cualquier explorador de archivos: 

* Haga doble click para abrir un archivo 

* Presione Ctrl+Click para seleccionar varios archivos 

* Presione Alt+Click para seleccionar el conjunto de archivos comprendido entre ambos clics. 

* Arrastre un archivo dentro del panel para copiarlo dentro de la carpeta seleccionada en el explorador de ficheros 

* Seleccione y arrastre un archivo del explorador de ficheros a una ventana externa al programa para moverlo/utilizarlo. 

* Los archivos mal nombrados se muestran con el texto de color rojo. 


### Barra de Menus 

La “Barra de Menus” se sitúa en la parte superior de la aplicación y tiene la siguiente disposición: 

![Toolbar menu](img/toolbar-menu.png "Toolbar menu")

* File: contiene tres acciones: 
  * Update pipeline: Cuando haya alguna actualización de GwaIO se deberá pulsar este botón para obtenerla. 

  * Remove empty folders: Elimina directorios vacíos que existan dentro del proyecto. 

  * Run tests: Esta opción es para los desarrolladores y no tiene ningún uso práctico para el usuario. 

* View: Activa o desactiva la visibilidad de paneles 

* Plugins: Inicializa el plugin seleccionado. Solo se puede inicializar un plugin a la vez. 

* <"Nombre del Proyecto">: Activa o desactiva las "Barras de herramientas" de cada proyecto. 

* Help: Muestra el dialogo de ayuda, hasta la fecha sólo tiene un “About”. 

### Barra de Estado 

Muestra diversos mensajes dependiendo de cuál sea la última acción hecha por el artista. 

## Barras de herramientas 

Las barras de herramientas, también conocidas como “toolbars” se pueden ocultar, mostrar, desacoplar de la interfaz o mover de posición al gusto del usuario. Cada una de estas barras de herramientas contienen bonotes con funcionalidades que se describen a continuación. 

![Multiples toolbars](img/multiples-toolbars.png "Multiples toolbars")

Algunas barras de herramientas (Toolbars). 

 

Para mostrar/ocultar las barras de herramientas, haga clic en Toolbars y/o <"Nombre del proyecto">, que se encuentra en la barra de menus, en la parte superior de la ventana, y seleccione o deseleccione las barras de herramientas que desee modificar. 

### Barra de herramientas del explorador 

Tiene funcionalidades relacionas con el manejo de ficheros. Además, tiene herramientas relacionadas con la publicación de versiones dentro de una base de datos. 


### Barra de herramientas de sincronización 

Tiene funcionalidades relacionadas con la sincronización de los sistemas de ficheros local y del servidor. 

### Barra de herramientas de reproducción 

Contiene herramientas relacionadas con la visualización y comprobación de ficheros. 

### Barra de herramientas de SG 

Contiene funcionalidades relacionadas con Shotgrid. 

## Paneles secundarios 

Los paneles secundarios muestran información adicional de las tareas y contienen herramientas de utilidad para facilitar el trabajo. 

![Dock panels](img/multiples-dock-panels.png "Dock panels")  
Algunos paneles secundarios agrupados. 

Estos paneles y barras de herramientas se pueden ocultar, mostrar, agrupar o desacoplar de la interfaz o mover de posición al gusto del usuario: 

* Si desea convertir un panel en flotante, haga clic en la barra de título y arrastre el panel a otra ubicación. Otro método para desacoplar un panel de forma automática es hacer doble clic en el título del panel. 

* Si desea acoplar un panel flotante, haga clic en la barra de título del panel y arrastre hacia otro panel hacia el borde de la ventana. Otro método para acoplar un panel de forma automática es hacer doble clic sobre la barra de título del panel. 

* Para mostrar/ocultar los paneles, haga clic en View, que se encuentra en la barra de menú en la parte superior de la ventana, y seleccione o deseleccione los paneles que desee modificar. 

### Panel de Configuración 

En este panel puede ver la información de la configuración del programa. Generalmente no se debería editar directamente, ya que se edita automáticamente con el uso del propio programa. 

### Panel de Filtrado 

Permite al usuario filtrar las tareas visibles en el “Panel de Tareas”. Hay un filtro por cada columna que aparece en este panel. Los filtros se pueden combinar entre sí. Cuando un filtro este activo su campo de texto es de color azul. 

![Panel Filter](img/panel-filter-general-interface.png "Panel Filter") 

Active la casilla “is not” para invertir el filtro. Esta acción hace que se invierta su funcionamiento y nos muestre las tareas que no contengan el texto introducido en el filtro. Esta acción cambia el color del campo del filtro a marrón. 

![Panel filter 'is not' actived](img/panel-filter-is-not-actived.png "Panel filter 'is not' actived")  
![Panel filter actived](img/panel-filter-actived.png "Panel filter actived") 

Haga clic en el icono de la “x” situado a la derecha del filtro para borrar por completo el texto. Alternativamente también puede el usuario borrarlo manualmente con las herramientas comunes de edición de texto. 

Los filtros tienen un sistema para autocompletar. Puede añadir varios tags de filtro separándo dichos tags con el signo “;”. 

![Panel filter multiples tags](img/panel-filter-multiples-tags.png "Panel filter multiples tags") 

Si el usuario activa la casilla “is not” y deja vacío el filtro, el “Panel de Tareas” no mostrará ninguna tarea. 

### Panel de Hilos 

Panel técnico donde se muestra el listado de todos los hilos de proceso abiertos, finalizados y a la espera en el programa. No es relevante para el usuario. 

 
![Panel Threads](img/panel-threads-general-interface.png "Panel Threads") 
 

### Panel de Sincronización 

Panel técnico donde se muestra el log de los archivos y carpetas sincronizadas. Además, este panel contiene los mismos botones de sincronizado de la "Barra de herramientas de sincronización". 

### Panel de Reproducción 

Reproductor y visualizador de contenido multimedia. Reproduce el último fichero seleccionado en el “Panel de Ficheros”. También reproduce la miniatura (si la hay en el sistema de ficheros local) de la última tarea seleccionada. 

### Panel de Notas 

Panel que recoge todas las notas que contenga la tarea seleccionada en el “Panel de Tareas”. Haga clic en una nota o imagen para abrirla en el navegador web. Adicionalmente, en la parte superior del panel se muestra la descripción de la tarea, si la tiene. 