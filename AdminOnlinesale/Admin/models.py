from django.db import models

class MerchantModel(models.Model):
    merchant_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30,default=False)
    contact_no=models.IntegerField(unique=True)
    email_id=models.EmailField(max_length=30,unique=True)
    def __str__(self):
        return self.name


class ProductModel(models.Model):
    product_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,unique=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    merchant=models.ForeignKey(MerchantModel,on_delete=models.CASCADE)


class CoustemerModel(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(max_length=120,unique=True)
    password=models.CharField(max_length=40)
    address=models.TextField(max_length=100)
    status=models.CharField(max_length=15,default='Active')

class SalesModel(models.Model):
    sales_id=models.AutoField(primary_key=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    merchant=models.ForeignKey(MerchantModel,on_delete=models.CASCADE)
    date=models.DateField()
    coustemer=models.ForeignKey(CoustemerModel,on_delete=models.CASCADE)
    amount=models.IntegerField()
