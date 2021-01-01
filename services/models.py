from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=111)
    Email=models.EmailField()
    Phone=models.IntegerField(max_length=12)
    Type=models.CharField(max_length=32)

    def __str__(self):
        return self.Name
