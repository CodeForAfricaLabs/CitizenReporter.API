from django.db.models.signals import post_save
from .models import Assignment

def assignment_callback(sender, **kwargs):
    print "Assignment Created!"

post_save.connect(assignment_callback, sender=Assignment, dispatch_uid="onAssignmentCreate")
