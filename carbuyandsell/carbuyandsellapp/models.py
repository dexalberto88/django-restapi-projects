from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    sold = models.BooleanField(default=False)
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.brand + " " + self.model + " " + self.brand + " " + f"{self.year}"