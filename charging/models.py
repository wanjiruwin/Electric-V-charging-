from django.db import models
from django.core.validators import MinValueValidator

class ChargingStation(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_charging_points = models.IntegerField(validators=[MinValueValidator(1)])
    available_charging_points = models.IntegerField(validators=[MinValueValidator(0)])
    is_operational = models.BooleanField(default=True)
    
    # Connector type choices
    CONNECTOR_CHOICES = [
        ('Type1', 'Type 1 (SAE J1772)'),
        ('Type2', 'Type 2 (Mennekes)'),
        ('CCS', 'Combined Charging System (CCS)'),
        ('CHAdeMO', 'CHAdeMO'),
        ('Tesla', 'Tesla Connector'),
    ]
    connector_type = models.CharField(
        max_length=20, 
        choices=CONNECTOR_CHOICES, 
        default='Type2'
    )
    
    def __str__(self):
        return f"{self.name} - {self.address}"
