#create a new component

python manage.py startapp agents 

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
   