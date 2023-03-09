# Proyecto Final Coderhouse Cristian-Murua

Integrantes:<br>
  Cristian Murua<br>

Descripcion del Proyecto:<br>
  Marketplace interactivo para usuarios registrados.<br>
  Funcionalidades:<br>
    -Visualizacion de productos publicados por los usuarios y busqueda mediante SearchBar<br>
    -Pagina de registro y login<br>
    -Visualizacion de productos propios<br>
    -funcionalidad para comentar publicaciones y likes de los comentarios<br>
    -chat integrado para dialogar con el vendedor del producto<br>
    -Inbox de mensajeria directa (chats)<br>
    -edicion de producto publicado<br>
    -edicion de datos de usuario<br>
    -Pagina About con info del desarrollador<br>
    -Pagina 404 Not Found demostrativa<br>
   <hr>
  Arquitectura:<br>
    Proyecto base<br>
    App 'Project' de productos (CRUD completo), comentarios y likes (test unitarios incluidos)<br>
    App 'Accounts' de registro, login, logout y avatar de usuario<br>
    App 'Messages' de chat e inbox<br>
    (implementacion de ajax con logica JavaScript para comentarios, likes y chat)<br>
    <hr>
  Rutas:<br>
    Project rutas<br>
    Home -> 'http://127.0.0.1:8000/' (barra de busqueda de productos integrada)<br>
    About -> 'http://127.0.0.1:8000/about/'<br>
    NotFound -> 'http://127.0.0.1:8000/not-found/'<br>
    Mis Productos (Logueo requerido) -> 'http://127.0.0.1:8000/my-products/'<br>
    Detalle de Producto -> 'http://127.0.0.1:8000/product/<id>/' (sistema de comentarios y likes integrado - Logueo requerido)<br>
    Mis Comentarios -> 'http://127.0.0.1:8000/comment-list/' (Logueo requerido)<br>
    Creacion de Producto -> 'http://127.0.0.1:8000/new-product/' (Logueo requerido)<br>
    Actualizacion de Producto -> 'http://127.0.0.1:8000/update-product/<id>/' (Logueo requerido)<br>
    Eliminacion de Producto -> 'http://127.0.0.1:8000/delete-product/<id>/' (Logueo requerido)<br>
    Eliminacion de Comentario -> 'http://127.0.0.1:8000/delete-comment/<id>' (Logueo requerido)<br>
    <br>
    <hr>
    <br>
    Accounts rutas<br>
    Sigup -> 'http://127.0.0.1:8000/signup/'<br>
    Login -> 'http://127.0.0.1:8000/login/'<br>
    Logout -> 'http://127.0.0.1:8000/logout/'<br>
    Edicion de Usuario -> 'http://127.0.0.1:8000/user-edit/'<br>
    Edicion de campos extra de Usuario -> 'http://127.0.0.1:8000/user-extra/'<br>
    Edicion de avatar de Usuario -> 'http://127.0.0.1:8000/avatar-edit/'<br>
    Detalle de Usuario (Vendedor) -> 'http://127.0.0.1:8000/user-detail/<id>/'<br>
    <hr>
    Messages rutas<br>
    Inbox -> 'http://127.0.0.1:8000/inbox/' (Logueo requerido)<br>
    Mensaje directo con usuario -> 'http://127.0.0.1:8000/dm/<nombre de usuario> (integrado en detalle de producto)<br>
    <hr>
    path de test unitarios:<br>
      Proyecto/ProyectoFinal/Project/test.py<br>
      <hr>
      
   Como correr el proyecto:<br>
      -clonar repositorio en su ordenador<br>
      -desde una consola (ej. cmd, powershell o bash para windows) ubicarse en ...\Proyecto><br>
      -crear entorno virtual (para instalar python pip install virtualenv) -> ...\Proyecto> virtualenv venv<br>
      -activar entorno virtual -> ...\Poryecto> venv/Scripts/activate<br>
      -deberia visualizar la consola con el entorno virtaul activado -> (venv) ...\Proyecto><br>
      -ingresar a la carpeta del proyecto -> cd ProyectoFinal<br>
      -instalar las dependencias necesarias -> python pip install -r requirements.txt<br>
      -correr server del proyecto -> python manage.py runserver<br>
    
    
    
    
    


 
