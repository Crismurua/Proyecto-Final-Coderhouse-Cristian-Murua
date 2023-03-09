# Proyecto Final Coderhouse Cristian-Murua

Integrantes:
  Cristian Murua

Descripcion del Proyecto:
  Marketplace interactivo para usuarios registrados.
  Funcionalidades:
    -Visualizacion de productos publicados por los usuarios y busqueda mediante SearchBar
    -Pagina de registro y login
    -Visualizacion de productos propios
    -funcionalidad para comentar publicaciones y likes de los comentarios
    -chat integrado para dialogar con el vendedor del producto
    -Inbox de mensajeria directa (chats)
    -edicion de producto publicado
    -edicion de datos de usuario
    -Pagina About con info del desarrollador
    -Pagina 404 Not Found demostrativa
   
  Arquitectura:
    Proyecto base
    App 'Project' de productos (CRUD completo), comentarios y likes (test unitarios incluidos)
    App 'Accounts' de registro, login, logout y avatar de usuario
    App 'Messages' de chat e inbox
    (implementacion de ajax con logica JavaScript para comentarios, likes y chat)
    
  Rutas:
    Project rutas
    Home -> 'http://127.0.0.1:8000/' (barra de busqueda de productos integrada)
    About -> 'http://127.0.0.1:8000/about/'
    NotFound -> 'http://127.0.0.1:8000/not-found/'
    Mis Productos (Logueo requerido) -> 'http://127.0.0.1:8000/my-products/'
    Detalle de Producto -> 'http://127.0.0.1:8000/product/<id>/' (sistema de comentarios y likes integrado - Logueo requerido)
    Mis Comentarios -> 'http://127.0.0.1:8000/comment-list/' (Logueo requerido)
    Creacion de Producto -> 'http://127.0.0.1:8000/new-product/' (Logueo requerido)
    Actualizacion de Producto -> 'http://127.0.0.1:8000/update-product/<id>/' (Logueo requerido)
    Eliminacion de Producto -> 'http://127.0.0.1:8000/delete-product/<id>/' (Logueo requerido)
    Eliminacion de Comentario -> 'http://127.0.0.1:8000/delete-comment/<id>' (Logueo requerido)
    
    
    
    Accounts rutas
    Sigup -> 'http://127.0.0.1:8000/signup/'
    Login -> 'http://127.0.0.1:8000/login/'
    Logout -> 'http://127.0.0.1:8000/logout/'
    Edicion de Usuario -> 'http://127.0.0.1:8000/user-edit/'
    Edicion de campos extra de Usuario -> 'http://127.0.0.1:8000/user-extra/'
    Edicion de avatar de Usuario -> 'http://127.0.0.1:8000/avatar-edit/'
    Detalle de Usuario (Vendedor) -> 'http://127.0.0.1:8000/user-detail/<id>/'
    
    Messages rutas
    Inbox -> 'http://127.0.0.1:8000/inbox/' (Logueo requerido)
    Mensaje directo con usuario -> 'http://127.0.0.1:8000/dm/<nombre de usuario> (integrado en detalle de producto)
    
    path de test unitarios:
      Proyecto/ProyectoFinal/Project/test.py
      
      
   Como correr el proyecto:
      -clonar repositorio en su ordenador
      -desde una consola (ej. cmd, powershell o bash para windows) ubicarse en ...\Proyecto>
      -crear entorno virtual (para instalar python pip install virtualenv) -> ...\Proyecto> virtualenv venv
      -activar entorno virtual -> ...\Poryecto> venv/Scripts/activate
      -deberia visualizar la consola con el entorno virtaul activado -> (venv) ...\Proyecto>
      -ingresar a la carpeta del proyecto -> cd ProyectoFinal
      -instalar las dependencias necesarias -> python pip install -r requirements.txt
      -correr server del proyecto -> python manage.py runserver
    
    
    
    
    


 
