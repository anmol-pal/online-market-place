# online-market-place

Creating and activating python env
Note there's no conda env active , if so  use <code>conda deactivate</code>
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
Updating database with new models added [Category]
1. Create Model [models.py](marketplaceProject/item/models.py)
2. Run <code>python3 manage.py makemigrations</code>
   This Will create a new table <code>Category</code> with field <b>id</b> and <b>name</b>
    ```
    (marketplace) anmolpal@Anmols-MacBook-Air marketplaceProject % python3 manage.py makemigrations

    Migrations for 'item':
    item/migrations/0001_initial.py
        - Create model Category
    ```
3. Applying them creates new tables <code>python manage.py migrate</code>
    ```
    (marketplace) anmolpal@Anmols-MacBook-Air marketplaceProject % python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, item, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying item.0001_initial... OK
    Applying sessions.0001_initial... OK
    ```
4. Creating Super User to access Django Database <code>python3 manage.py createsuperuser</code>
    ```
    $ python3 manage.py createsuperuser 
    Username (leave blank to use 'anmolpal'): admin
    Email address: admin@marketplace.com
    Password: <super@123>
    Password (again): <super@123>
    Superuser created successfully.
    ```
    Access Django administration as
    ```
    % python manage.py runserver 
    <truncated output>
    Starting development server at http://127.0.0.1:8000/
    ```
5. Access Database here [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
6. Register Models in [admin.py](marketplaceProject/item/admin.py)
    ```
    from .models import Category
    admin.site.register(Category)
    ```
7. Check if a new table appears in database.