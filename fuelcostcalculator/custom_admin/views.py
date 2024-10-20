from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from calculator.models import BikeModel, FuelPrice, BikeBrand 
from django.contrib.auth.models import User
from django import forms

# Restrict access to superusers only
def admin_only(user):
    return user.is_superuser

@user_passes_test(admin_only)
def dashboard(request):
    bikes = BikeModel.objects.all()  # Assuming this is what you want to show
    users = User.objects.all()
    return render(request, 'custom_admin/dashboard.html', {'bikes': bikes, 'users': users})


@user_passes_test(admin_only)
def manage_bikes(request):
    bike_models = BikeModel.objects.all()
    bike_brands = BikeBrand.objects.all()  # Fetch all bike brands

    if request.method == 'POST':
        # Check for adding a bike model
        if 'model_name' in request.POST:
            model_name = request.POST.get('model_name')
            brand_id = request.POST.get('brand')
            fuel_efficiency = request.POST.get('fuel_efficiency')
            image = request.FILES.get('image')

            BikeModel.objects.create(
                model_name=model_name,
                brand_id=brand_id,
                fuel_efficiency=fuel_efficiency,
                image=image
            )
            return redirect('custom_admin:manage_bikes')

        # Check for adding a bike brand
        elif 'brand_name' in request.POST:
            brand_name = request.POST.get('brand_name')
            BikeBrand.objects.create(brand_name=brand_name)
            return redirect('custom_admin:manage_bikes')

    return render(request, 'custom_admin/manage_bikes.html', {
        'bike_models': bike_models,
        'bike_brands': bike_brands
    })
@user_passes_test(admin_only)
def add_bike_model(request):
    if request.method == 'POST':
        name = request.POST.get('model_name')  # Ensure this matches your form field name
        brand_id = request.POST.get('brand')  # Assume you have a dropdown for brand
        fuel_efficiency = request.POST.get('fuel_efficiency')
        image = request.FILES.get('image')  # For image upload

        # Create new BikeModel
        BikeModel.objects.create(
            model_name=name,
            brand_id=brand_id,
            fuel_efficiency=fuel_efficiency,
            image=image
        )
        return redirect('custom_admin:manage_bikes')

    return render(request, 'custom_admin/add_bike_model.html')  # Create this template for the form

@user_passes_test(admin_only)
def edit_bike_model(request, bike_model_id):
    bike_model = get_object_or_404(BikeModel, id=bike_model_id)
    bike_brands = BikeBrand.objects.all()  # Get all bike brands
    
    if request.method == 'POST':
        bike_model.model_name = request.POST.get('model_name')
        bike_model.brand_id = request.POST.get('brand')
        bike_model.fuel_efficiency = request.POST.get('fuel_efficiency')
        
        if 'image' in request.FILES:  # Check if an image is uploaded
            bike_model.image = request.FILES['image']
        
        bike_model.save()
        return redirect('custom_admin:manage_bikes')

    return render(request, 'custom_admin/edit_bike_model.html', {
        'bike_model': bike_model,
        'bike_brands': bike_brands  # Pass bike brands to the template
    })

@user_passes_test(admin_only)
def delete_bike_model(request, bike_model_id):
    bike_model = get_object_or_404(BikeModel, id=bike_model_id)
    bike_model.delete()
    return redirect('custom_admin:manage_bikes')

@user_passes_test(admin_only)
def manage_fuel_price(request):
    fuel_prices = FuelPrice.objects.all()
    return render(request, 'custom_admin/manage_fuel_price.html', {'fuel_prices': fuel_prices})

@user_passes_test(admin_only)
def add_fuel_price(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        FuelPrice.objects.create(price=price)
        return redirect('custom_admin:manage_fuel_price')

    return render(request, 'custom_admin/add_fuel_price.html')  # Create this template for the form

@user_passes_test(admin_only)
def edit_fuel_price(request, fuel_price_id):
    fuel_price = get_object_or_404(FuelPrice, id=fuel_price_id)
    
    if request.method == 'POST':
        fuel_price.price = request.POST.get('price')
        fuel_price.save()
        return redirect('custom_admin:manage_fuel_price')

    return render(request, 'custom_admin/edit_fuel_price.html', {'fuel_price': fuel_price})

@user_passes_test(admin_only)
def delete_fuel_price(request, fuel_price_id):
    fuel_price = get_object_or_404(FuelPrice, id=fuel_price_id)
    fuel_price.delete()
    return redirect('custom_admin:manage_fuel_price')
