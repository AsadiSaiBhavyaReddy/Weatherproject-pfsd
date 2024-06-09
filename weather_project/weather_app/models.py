from django.db import models



class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)  # admin
    password = models.CharField(max_length=100, blank=False)  # admin

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)  # admin
    password = models.CharField(max_length=100, blank=False)  # admin

    class Meta:
        db_table = "user_table"

    def __str__(self):
        return self.username