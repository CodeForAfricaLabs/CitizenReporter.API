from django.apps import AppConfig
from django.db.models.signals import post_save
from .signals import assignment_callback
from .models import Assignment


class AssignmentsConfig(AppConfig):
    name = 'assignments'

    def ready(self):
        post_save.connect(assignment_callback, sender=Assignment, dispatch_uid="assignment_callback")
