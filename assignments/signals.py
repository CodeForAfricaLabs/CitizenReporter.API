from django.db.models.signals import post_save
from .models import Assignment

def assignment_callback(sender, created, **kwargs):
    if created:
        print "Assignment Created!"
