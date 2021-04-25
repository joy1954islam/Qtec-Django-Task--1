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
        with_out_total_price = request.POST['with_out_total_price']
        with_return_total_price = request.POST['with_total_price']
        parcel = Parcel()
        parcel.merchant = merchant
        parcel.product_type = product_type
        parcel.zone = zone
        parcel.unit = unit
        parcel.with_out_return_total_price = with_out_total_price
        parcel.with_return_total_price = with_return_total_price
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
    charges = Charge.objects.get(zone=zone, unit=unit)
    zone_name = charges.zone.zone_name
    if zone_name == 'Inside of Dhaka':
        price = charges.price
        return JsonResponse({'with_out_total_price': price, 'with_total_price': price}, safe=False)
    else:
        price = charges.price + charges.price * 0.01
        with_total_price = price + price * 0.5
        return JsonResponse({'with_out_total_price': price, 'with_total_price': with_total_price}, safe=False)
