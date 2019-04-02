from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.email, self.name)

class Entries(models.Model):
    type = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.type, self.amount, self.user_id)
