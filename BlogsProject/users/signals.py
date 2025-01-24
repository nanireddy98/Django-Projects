from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Signal to create a Profile instance whenever a new User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile object for a new User instance.

    Args:
        sender: The model class sending the signal (User).
        instance: The actual User instance being saved.
        created: Boolean indicating whether a new instance was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)


# Signal to save the Profile instance whenever the User instance is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Saves the associated Profile object whenever the User instance is saved.

    Args:
        sender: The model class sending the signal (User).
        instance: The actual User instance being saved.
        **kwargs: Additional keyword arguments.
    """
    instance.profile.save()
