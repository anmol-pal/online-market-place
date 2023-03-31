# online-market-place

Creating and activating python env
Note there's no conda env active , if so  use <code>conda deactivate<code>
```
python3 -m venv marketplace
source marketplace/bin/activate
(marketplace) anmolpal@Anmols-MacBook-Air online-market-place 
```
Install Django in virtual environment
```
pip3 install Django
```
Create a Django-Project
    This will create a folder with name marketplaceProject and a manage.py
```
django-admin startproject marketplaceProject
```

manage.py - is a script for running admin tasks like updating DB, adding super user , running dev server etc etc
asgi.py - entry points for the server
wsgi.py - entry points for the server
settings.py - global config for entire project
urls.py - like a table of content for entire project, links URL to a specific vew

To start the server
```
cd marketplaceProject
python3 manage.py runserver
```

We can divide Django app into different modules 
```
python manage.py startapp core
```
This creates a new module (Django App)
    - migrations : will store information about database
    - admin.py : to store register database models to be used inside django admin interface.
    - apps.py : configuration file for the specific app (core)
    - models.py : define database models , information about what we want to store 
    - tests.py : to run automated tests
    - views.py : for views , Django will look for a folder templates for rendering the file
To use your app ,  add an entry in settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```
Making migrations - updating database with new models added

Will create a new table <code>Category</code> with field <b>id</b> and <b>name</b>
```
(marketplace) anmolpal@Anmols-MacBook-Air marketplaceProject % python3 manage.py makemigrations

Migrations for 'item':
  item/migrations/0001_initial.py
    - Create model Category
```
