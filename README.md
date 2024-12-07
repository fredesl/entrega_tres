Tienda HeMan

Este proyecto es una aplicación web desarrollada en Django para gestionar una tienda. Permite administrar clientes, productos y sucursales a través de formularios específicos y plantillas personalizadas.

Características

•	Gestión de clientes, productos y sucursales.

•	Formularios accesibles desde URLs dedicadas para agregar datos.

•	Organización modular utilizando el framework Django.
________________________________________

Requisitos previos

Asegúrate de tener instalado lo siguiente antes de empezar:

•	Python 3.8 o superior.

•	Django 4.x (puedes verificar la versión exacta en requirements.txt).

•	Un entorno virtual configurado (opcional pero recomendado).

________________________________________
Instalación

1.	Clona este repositorio:

git clone https://github.com/fredesl/pre_entrega3.git

cd fredesl

2.	Crea y activa un entorno virtual:
	
python -m venv env

source env/bin/activate 

env\Scripts\activate

3.	Realiza las migraciones:

python manage.py makemigrations

python manage.py migrate

4.	Inicia el servidor de desarrollo:

python manage.py runserver

Luego, visita:

http://127.0.0.1:8000/ en tu navegador.
________________________________________


Modelos Principales

El proyecto cuenta con los siguientes modelos:

1.	Cliente
   
o Representa a los clientes de la tienda.

o	Campos: Nombre, Apellido, Email, Posición IVA.

2.	Producto
   
o	Representa los productos disponibles en la tienda.

o	Campos: Nombre, Descripción, Precio, Cantidad.

3.	Sucursal
   
o	Representa las diferentes sucursales de la tienda.

o	Campos: Nombre, Dirección, Provincia.
________________________________________
Formularios y URLs

Cada modelo tiene un formulario accesible desde una URL específica:

•	Clientes:


o	URL: http://127.0.0.1:8000/clientes/

o	Descripción: Formulario para ver el listado de clientes.

o	URL: http://127.0.0.1:8000/agregar-cliente

o	Descripción: Formulario para agregar nuevos clientes.

•	Productos:


o	URL: http://127.0.0.1:8000/productos/

o	Descripción: Formulario para ver el listado de productos.

o	URL: http://127.0.0.1:8000/agregar-producto

o	Descripción: Formulario para agregar nuevos productos.

•	Sucursales:


o	URL: http://127.0.0.1:8000/sucursales/

o	Descripción: Formulario para ver el listado de sucursales.

o	URL: http://127.0.0.1:8000/agregar-sucursal

o	Descripción: Formulario para agregar nuevas sucursales.
