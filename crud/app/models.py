from django.db import models # type: ignore

class Operations(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
