from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
         abstract = True

class Users(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.email, self.name)

class Entries(TimeStampedModel):
    type = models.CharField(max_length=255, null=False)
    amount = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


    def __str__(self):
        return "{} - {}".format(self.type, self.amount, self.user_id)
