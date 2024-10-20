from django.contrib import admin
from django.utils.html import format_html
from .models import Bike, Trip, MaintenanceSchedule, BikeModel, FuelPrice, BikeBrand


class MaintenanceScheduleInline(admin.TabularInline):
    model = MaintenanceSchedule
    extra = 1  # Number of empty forms to display

# Admin for BikeModel with correct field names
@admin.register(BikeModel)
class BikeModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'fuel_efficiency', 'display_image')  # Show 'model_name', 'brand', and 'display_image'
    search_fields = ('model_name', 'brand__brand_name', 'fuel_efficiency')  # Search by model name and brand name

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'No image'  # or return an empty string if you prefer

    display_image.short_description = 'Image' 

# Admin for FuelPrice
@admin.register(FuelPrice)
class FuelPriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'effective_date')  # Show the price and effective date
    ordering = ('-effective_date',)  # Order by most recent first
    search_fields = ('price',)  # Add a search box for quick filtering

# Admin for Bike
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'model', 'vehicle_number', 'exhaust_type', 'air_filter_type', 'tire_size')  # Include 'vehicle_number'
    list_filter = ('owner', 'model', 'exhaust_type', 'air_filter_type')  # Add filters for easy access
    search_fields = ('owner__username', 'model__model_name', 'vehicle_number')  # Search by owner, model name, and vehicle number
    inlines = [MaintenanceScheduleInline]  # Inline for maintenance schedules

# Admin for Trip
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('owner', 'bike', 'start_location', 'end_location', 'distance', 'fuel_cost', 'rider_weight','calculated_FE')  # Added rider_weight
    list_filter = ('owner', 'bike')  # Add filters for easy access
    search_fields = ('start_location', 'end_location', 'bike__model__model_name')  # Search by start, end location, and bike model

# Admin for MaintenanceSchedule
@admin.register(MaintenanceSchedule)
class MaintenanceScheduleAdmin(admin.ModelAdmin):
    list_display = ('bike', 'service_date', 'service_description', 'reminder_sent')
    list_filter = ('bike', 'service_date')  # Add filters for easy access
    search_fields = ('service_description', 'bike__model__model_name')  # Search by service description and bike model

# Admin for BikeBrand
@admin.register(BikeBrand)
class BikeBrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)  # Updated to use 'name' assuming this is the field in the BikeBrand model
    search_fields = ('brand_name',)  # Search by brand name
