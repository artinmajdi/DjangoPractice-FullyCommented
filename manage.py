#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


""" Test publishign feature """

""" Activate the environment by coppying the command below in terminal """
    # source /Users/artinmac/GoogleDrive/RESEARCH/Learning/CodePractice/Django/envPy_django/bin/activate

""" After I created my app models and added them to the settings->INSTALLED_APPS, 
    I will need a database table for them. Django comes with a migration system that 
    tracks the changes made to models and enables them to propagate into the database. 
    As mentioned, the migrate command applies migrations for all applications listed 
    in INSTALLED_APPS; it synchronizes the database with the current models and existing 
    migrations.
    1.  First, I need to create an initial migration for your Post model. In the 
        root directory of your project, run the below command. This will cause Django 
        will create a 0001_initial.py file inside the migrations directory of my application.
            >> python manage.py makemigrations blog
            
        A migration specifies dependencies on other migrations and operations to perform 
        in the database to synchronize it with model changes.
    
    2.  Django will execute SQL code in the database to create the table for your model. 
        The sqlmigrate command takes the migration names and returns their SQL without executing it. 
        Run the following command to inspect the SQL output of your first migration:
            >> python manage.py sqlmigrate blog 0001
            
    3.  Sync the database using below code. Django will apply migrations for the applications 
        listed in INSTALLED_APPS. After applying the migrations, the database reflects the current status of models.
            >> python manage.py migrate
            
    Changing the Models:
    
        If I edit the models.py file in order to add, remove, or change the fields of existing 
        models, or if I add new models, I will have to create a new migration using the makemigrations 
        command. The migration will allow Django to keep track of model changes. Then, you will have to 
        apply it with the migrate command to keep the database in sync with my models.

    4.  Creating an administration site for models:
        Now that you have defined the Post model, you will create a simple administration site to 
        manage your blog posts. Django comes with a built-in administration interface that is very 
        useful for editing content. The Django site is built dynamically by reading your model 
        metadata and providing a production-ready interface for editing content. You can use it 
        out of the box, configuring how you want your models to be displayed in it. 
        
        The django.contrib.admin application is already included in the INSTALLED_APPS setting, so 
        you don't need to add it.
        
        a.  Creating a superuser: First, you will need to create a user to manage the administration site. Run the following command:
                >> python manage.py createsuperuser
                    username: artinmac
                    password: >

        b.  Django administration site: 
                Start the development server:
                    >> python manage.py runserver 
                Go to http://127.0.0.1:8000/admin/ 
            
            In the page you can see Group and User models you created as part of the Django authentication 
            framework located in django.contrib.auth. If you click on Users, you will see the user you created previously.

        c.  Adding models to the administration site:
            To add your app models to the administration site. Edit the admin.py file of the application and 
            add codes below
                >> from django.contrib import admin
                >> from .models import <model-name-inside-app> (e.g. Post)
                >> admin.site.register( <model-name-inside-app> )
            
    Customizing the way that models are displayed:
        ...  Continue From https://learning.oreilly.com/library/view/django-3-by/9781838981952/Text/Chapter_1.xhtml#_idParaDest-14 ...
        
"""


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    

