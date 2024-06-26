from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
