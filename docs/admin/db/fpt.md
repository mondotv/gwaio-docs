# Flow Production Tracking (ShotGrid)

Antes de sincronizar GwaIO con Flow Production Tracking debes preparar el esquema en la base de datos de Flow:

- Crea la entidad personalizada **GwaIO User** (CustomEntity) para mapear usuarios de GwaIO con artistas en Flow.
- Añade el campo de relación `gwaio_user` en todas las entidades que necesiten asignar a un usuario de GwaIO (Tasks, Assets, PublishedFiles, Timelogs, etc.).
- Utiliza tanto la configuración del estudio como la de los proyectos para setear los valores necesarios para comunicar GwaIO con Flow mediante el plugin.
- Revisa la documentación técnica para crear un plugin de proyecto para Flow/Shotgrid.
