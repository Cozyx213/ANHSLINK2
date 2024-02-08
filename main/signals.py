from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Resources

@receiver(post_delete, sender=Resources)
def delete_associated_file(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Resources` object is deleted.
    """
    if instance.file:
        # Get the path of the file
        file_path = instance.file.path
        # Check if the file exists
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)