from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    admin = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'User'