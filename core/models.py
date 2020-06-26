from django.db import models


class TestModel(models.Model):
    string = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.string}"
