#run the project 
python manage.py runserver

#create a new component

python manage.py startapp agents 

#add the new component to INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agent'
]

#export isntalled packages to requirements.txt file

pip freeze > requirements.txt

#run the test case

python manage.py test

#prepare for the db migrations

python manage.py makemigrations

#migrate the db

python manage.py migrate

#create superuser
python manage.py createsuperuser


#pass if the placeholder for future code
def my_fun():
    pass

#signals allow certain senders to notify a set of receivers that some action has taken place

from django.db.models.signals import post_save

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

#to collect all static files
python manage.py collectstatic
   