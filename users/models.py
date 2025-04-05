from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def assign_role(self, role_name):
        group, _ = Group.objects.get_or_create(name=role_name)
        self.groups.add(group)

    def __str__(self):
        return self.username


class FarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer_profile')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_link = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
