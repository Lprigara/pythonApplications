Primeros pasos:
# Aquí pondremos las instrucciones para poder ejecutar nuestra aplicación
1) Instrucción crear Entorno virtual virtualenv <nombre entorno>
2)  Instrucción entrar Entorno virtual  source venv/bin/activate
3)  Instrucción desactivar Entorno virtual   deactivate
4) Instrucción eliminar Entorno virtual  rm -rf <nombre entorno>
5) Crear el proyecto  django-admin startproject <nombre proyecto>
6) Crear la aplicación  django-admin startapp <nombre proyecto>
7) Instrucción para ejecutar el proyecto   python manage.py runserver
8) Instrucción crear archivo requirements.txt   pip freeze > requirements.txt
9) Instrucciones para migrar la base de datos. 
    python manage.py makemigrations
    python manage.py migrate
10) Instrucción crear un superusuario  python manage.py createsuperuser
# TODO: Instrucción para crear archivo de traducción
# TODO: Instrucción compilar la traducción
# TODO: Instrucción para eliminar el Entorno Virtual
