from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Neighborhood(models.Model):

  neighborhood_name = models.CharField(max_length=30)
  neighborhood_location = models.CharField(max_length=30)
  neighborhood_pic = ImageField(blank=True, manual_crop="1920x1080")
  occupants_count = models.IntegerField(null=True)
  police_contact = PhoneNumberField()
  health_contact = PhoneNumberField()

  @classmethod
  def get_all_neighborhoods(cls):
    neighborhoods = cls.objects.all()
    return neighborhoods