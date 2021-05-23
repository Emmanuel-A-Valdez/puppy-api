from django.db import models


class Puppy(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to="imgs",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

