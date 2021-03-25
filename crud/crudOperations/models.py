from django.db import models


# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"