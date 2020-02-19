# Senior Career Day - Workshop2020
Today will be using the MVC framework of Django to build a simple blog website.

## Prerequisites
Make sure you have Python3 installed on your computer.

## Get Started
First, we will want to create a virtual environment so any dependencies that we install will be limited to that environment.

### On Windows
    cd Desktop
    virtualenv env
    cd env
    Scripts\activate.bat

### On Mac/Linux
    mkdir workshop2020
    cd workshop2020
    python3 -m venv .env
    source .env/bin/activate

## Install Django
    pip install Django
    
## Create Project
    cd ../
    mkdir website
    cd website
    django-admin startproject website
    
## Create the Blog app
    cd website
    python manage.py startapp blog
    
Your directory structure should look like this:

    ├── db.sqlite3
    ├── website
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── manage.py
    └── blog
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
    
## Add Blog app to settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog'
    ]
    
### Migrate changes to the database
    python manage.py migrate

### Now let us test our site by running the server
    python manage.py runserver 0.0.0.0:8000
    
If you visit 0.0.0.0:8000 in your browser, you should see this:

<img src="workshop2020/website/static/images/initial_django.png">
