from django.db import models

# Create your models here.
class Messages(models.Model):
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.message

