#
from django.db import models


class Show(models.Model):
    image = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
