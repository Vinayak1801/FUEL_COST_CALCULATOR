from django.urls import path
from . import views
app_name = 'calculator' 
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Bike Management
    path('add_bike/', views.add_bike, name='add_bike'),
    path('bike/<int:bike_id>/', views.view_bike, name='view_bike'),
    path('bike/<int:bike_id>/delete/', views.delete_bike, name='delete_bike'),
    path('view_bikes/', views.view_bikes, name='view_bikes'),
    
    # Fuel Cost Calculation
    path('calculate_fuel/', views.calculate_fuel_cost, name='calculate_fuel'),
    
    # Maintenance Reminder
    path('maintenance_reminder/', views.maintenance_reminder, name='maintenance_reminder'),

    # AJAX URL for fetching bike models
    path('get_bike_models/', views.get_bike_models, name='get_bike_models'),

    #save trip
    path('save_trip/', views.save_trip, name='save_trip'),
    path('view_trips/', views.view_trips, name='view_trips'),

    
]
