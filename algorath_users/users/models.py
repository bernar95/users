
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.TextField(max_length=200)
    user_connection = models.ForeignKey('self', on_delete=models.DO_NOTHING)
