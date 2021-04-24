from django.db import models
import uuid


class Zone(models.Model):
    zone_name = models.CharField(max_length=150)

    def __str__(self):
        return self.zone_name


class Unit(models.Model):
    kg_choose = models.CharField(max_length=50)

    def __str__(self):
        return self.kg_choose


class Charge(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='charges')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return str(self.unit) + ' ' + str(self.zone)


class Merchant(models.Model):
    merchant_name = models.CharField(max_length=200)

    def __str__(self):
        return self.merchant_name


class Parcel(models.Model):
    product_type = (
        ('Fragile', 'Fragile'),
        ('Liquid', 'Liquid')
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20, choices=product_type)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    merchant_invoice_id = models.CharField(max_length=50, null=True, blank=True)
    total_price = models.FloatField()

    def __str__(self):
        return str(self.merchant)

    def save(self, *args, **kwargs):
        self.merchant_invoice_id = uuid.uuid4().hex
        super(Parcel, self).save(*args, **kwargs)



