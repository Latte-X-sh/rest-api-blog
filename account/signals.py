from django.contrib.auth.models import User   
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .models import Profile ,Post
    
"""
This file is responsible for describing signals,
where we have a sender who is responsible for
notifying the receiver when an event has occured
.
The receiver is responsible for performing an action
once the signal reaches it.
When a user object has been created , then the profile
model will be invoked to create a profile record
for the created user.

The django dispatch is responsible for connecting receivers 
and senders

"""

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    '''
    This signal fuction is reponsible for creating an instance
    of the profile model and save it into the db.
    It is wrapped by the receiver decorator that will invoke
    it once the Model User has created a user instance.
    
    Args:
    - Sender : model that notifies the function,when the user instance
    has been created.
    - instance: the user instance
    - created : a bool instance indicating whether the instance has been 
    created or not.
    
    Return:
        None
    '''
    if created:
        Profile.objects.create(user=instance)
        
        
@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    """
    This signal function, saves a  Profile instance when the User model
    is created.
    
    Args:
    - Sender : model that notifies the function,when the user instance
    has been created.
    - instance: the user instance
    """
    instance.profile.save()
    
    
@receiver(post_delete, sender=User)    
def destroy_profile(sender,instance,**kwargs):
    """
    This function is responsible for deleting the profile instance 
    when the user has been deleted. 

    Args:
    - Sender : model that notifies the function,when the user instance
    has been created.
    - instance: the user instance

    """
    instance.profile.delete()
    

