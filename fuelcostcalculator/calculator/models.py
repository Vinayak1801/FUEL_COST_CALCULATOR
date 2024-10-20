from django.db import models
from django.contrib.auth.models import User

# BikeBrand model to store different brands of bikes
class BikeBrand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand_name

# BikeModel model to store different bike models
class BikeModel(models.Model):
    model_name = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(BikeBrand, on_delete=models.CASCADE,null=True)  # Linking brand with BikeModel
    fuel_efficiency = models.FloatField(default=40)
    image = models.ImageField(upload_to='bike_images/', null=True, blank=True)  # Add an image field


    def __str__(self):
        return f"{self.brand.brand_name} {self.model_name}"

# FuelPrice Model to store fuel prices and their effective dates
class FuelPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.price} - Effective from {self.effective_date}"

    @classmethod
    def get_latest_price(cls):
        return cls.objects.latest('effective_date').price

# Bike model with ForeignKey to BikeModel, includes exhaust type, air filter type, etc.
class Bike(models.Model):
    EXHAUST_TYPES = (
        ('Stock', 'Stock'),
        ('Aftermarket', 'Aftermarket'),
    )
    AIR_FILTER_TYPES = (
        ('Stock', 'Stock'),
        ('High Performance', 'High Performance'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20, unique=True, null=True)  # Allowing null temporarily
    exhaust_type = models.CharField(max_length=20, choices=EXHAUST_TYPES)
    air_filter_type = models.CharField(max_length=20, choices=AIR_FILTER_TYPES)
    tire_size = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model.model_name} owned by {self.owner.username}"

# Trip model to store trip details including distance, fuel cost, etc.
class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.FloatField()
    fuel_cost = models.FloatField()
    rider_weight = models.FloatField(default=60)  # Default weight
    calculated_FE=models.FloatField(null=True)

    def __str__(self):
        return f"Trip from {self.start_location} to {self.end_location} by {self.bike.model.model_name}"

# Maintenance Schedule model to track bike service schedules and reminders
class MaintenanceSchedule(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_description = models.CharField(max_length=200)
    reminder_sent = models.BooleanField(default=False)
    next_service_date = models.DateField(null=True, blank=True)  # Optional field for next service

    def __str__(self):
        return f"Service for {self.bike.model.model_name} on {self.service_date}"
