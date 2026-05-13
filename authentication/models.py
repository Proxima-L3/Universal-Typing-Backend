from django.db import models

# Create your models here.

class UserAuthInfo(models.Model):

    user_username = models.CharField(max_length=25)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)

    # below not needed for django model classes

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fillerVars = ''