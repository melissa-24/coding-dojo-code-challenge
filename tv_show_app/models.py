from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # Setting length requirements
        if len(postData['title']) < 2:
            errors["show_title"] = "Title should be at least 2 caracters"
        if len(postData['network']) < 3:
            errors["network"] = "Network name shoud be at least 3 caracter"
        if len(postData['decription']) < 10:
            errors["decription"] = "Descriptions should be al least 10 characters"
        return errors
# creating the table
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    decription = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Shows object: {self.title} ({self.id})"