
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=200)
    user_connections = models.ManyToManyField('self', through='Connection', symmetrical=False,
                                              related_name='related_to')

    def __str__(self):
        return "ID: " + str(self.user_id) + ", Name: " + self.user_name


class Connection(models.Model):
    from_user = models.ForeignKey(User, related_name='from_users', on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(User, related_name='to_users', on_delete=models.DO_NOTHING)


