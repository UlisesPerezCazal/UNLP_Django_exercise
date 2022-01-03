# UNLP_Django_exercise


Clonar repositorio.

Para correr los comandos en consola vas a necesitar tener instalado Python (https://www.python.org/)

Instalar requirements:
    $ pip install -r requirement.txt

Se necesita levantar una base de datos, en mi caso usé postgreSQL(https://www.postgresql.org/download/). para levantar la base de datos:
    Crear un archivo .env en la capeta unlp_excercise/unlp_excercise con los siguentes parametros
        SECRET_KEY=
        DEBUG=True
        NAME=
        USER=
        PASSWORD=
        HOST=
        PORT=

asignarle los valores correspondientes a su configuracion de base de datos

Hacer las migraciones de los modelos:
    # Las migraciones se versionan y por lo tanto los otros devs SOLO deberian conrrer el migrate.
    $ python manage.py makemigrations
    $ python manage.py migrate
Esto creara la base de datos vacía con los modelos del proyecto, lista para ser populada.

Con el comando 
    $ python manage.py runserver

La API ya está funcionando!.
