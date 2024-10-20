from django import forms
from .models import BikeModel, FuelPrice, Bike, Trip

class BikeModelForm(forms.ModelForm):
    class Meta:
        model = BikeModel
        fields = ['model_name', 'brand', 'fuel_efficiency', 'image']

class FuelPriceForm(forms.ModelForm):
    class Meta:
        model = FuelPrice
        fields = ['price', 'effective_date']

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['owner', 'model', 'vehicle_number', 'exhaust_type', 'air_filter_type', 'tire_size']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['owner', 'bike', 'start_location', 'end_location', 'distance', 'fuel_cost', 'rider_weight']
