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

![Logging dock](img/logging-dock.png "Logged out state")


* Hola
  * que tal

1. Que tal
2. Como estas