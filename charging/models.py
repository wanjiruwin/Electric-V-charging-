from django.db import models

# Create your models here.
from django.db import models

class ChargingStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Under Maintenance', 'Under Maintenance')])
    image = models.ImageField(upload_to='stations/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

# Replace 'your_admin_username' with your actual admin username
user = User.objects.get(username='evadmin')

# Set a new password (replace 'new_password' with your desired password)
user.set_password('@shee123')
user.save()

from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
