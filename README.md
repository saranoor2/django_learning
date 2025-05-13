python3 -m venv env
source env/bin/activate

django-admin startproject advertisement .

python manage.py runserver

python manage.py startapp api 