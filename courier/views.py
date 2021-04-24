from django.shortcuts import render, redirect
from .models import Parcel, Charge, Merchant, Zone, Unit
from django.http import JsonResponse


def parcel_create(request):
    merchant = Merchant.objects.all()
    zone = Zone.objects.all()
    unit = Unit.objects.all()
    if request.method == "POST":
        merchant = Merchant.objects.get(id=request.POST['merchant'])
        product_type = request.POST['product_type']
        zone = Zone.objects.get(id=request.POST['zone'])
        unit = Unit.objects.get(id=request.POST['unit'])
        price = request.POST['total_price']
        parcel = Parcel()
        parcel.merchant = merchant
        parcel.product_type = product_type
        parcel.zone = zone
        parcel.unit = unit
        parcel.total_price = price
        parcel.save()
        return redirect('parcel_view')
    context = {
        'merchant': merchant,
        'zone': zone,
        'unit': unit,
    }
    return render(request, 'parcel_create_form.html', context=context)


def parcel_view(request):
    parcel = Parcel.objects.all()
    context = {
        'parcel': parcel
    }
    return render(request, 'parcel_list.html', context=context)


def total_price(request, zone, unit):
    print(zone, unit)
    charges = Charge.objects.get(zone=zone, unit=unit)
    print(charges)
    price = charges.price
    print(price)
    return JsonResponse({'total_price': price}, safe=False)
