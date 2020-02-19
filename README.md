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

### Now we need to define models in our database
    from django.db import models
    from django.contrib.auth.models import User


    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )

    class Post(models.Model):
        title = models.CharField(max_length=200, unique=True)
        slug = models.SlugField(max_length=200, unique=True)
        author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
        updated_on = models.DateTimeField(auto_now= True)
        content = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)
        status = models.IntegerField(choices=STATUS, default=0)

        class Meta:
            ordering = ['-created_on']

        def __str__(self):
            return self.title

#### And we need to migrate these changes
    python manage.py makemigrations
    python manage.py migrate

### Now we are going to edit the prebuilt admin portal, but first we need to create an admin account
    python manage.py createsuperuser
    
    Username (leave blank to use 'root'): admin
    Email address: admin@gamil.com
    Password: 
    Password (again):
    
### Visit the admin portal at 0.0.0.0:8000/admin
Log in using your credentials

<img src="workshop2020/website/static/images/login_screen.png">

Once you have logged in, you will see the admin portal

<img src="workshop2020/website/static/images/admin_portal.png">

### Next we want to register our Post model with the admin portal. In blog/admin.py add the following:
    from django.contrib import admin
    from .models import Post 

    # customizes the appearance of our model in the admin view
    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'slug', 'status','created_on')
        list_filter = ("status",)
        search_fields = ['title', 'content']
        prepopulated_fields = {'slug': ('title',)}

    # registers the model and its customizations with the admin portal
    admin.site.register(Post, PostAdmin)

Now, if we create a post, we will see it in our admin portal

<img src="workshop2020/website/static/images/post1.png">

<img src="workshop2020/website/static/images/post2.png">

<img src="workshop2020/website/static/images/post3.png">


