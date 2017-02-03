from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


def image_upload_to(instance, filename):
    return "images/%s" % filename


class File(models.Model):
    expiration_date = models.DateField()
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to=image_upload_to)
    cover = models.ImageField(upload_to=image_upload_to,null=True,blank=True)

    def __unicode__(self):
        return self.name
