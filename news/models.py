from django.db import models
import random


class tip_model(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):

        return self.subject
    def __unicode__(self):
        return self.subject
