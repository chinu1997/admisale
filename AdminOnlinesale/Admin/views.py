import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from.models import MerchantModel,ProductModel
from .forms import MerchantForm,ProductForm
# Create your views here.
def checkAdmin(request):
    idno=request.POST.get('uid')
    passd=request.POST.get('upsd')
    if idno == "chinmaya" and passd == 'chinu1997':
        return render(request,"index.html")
    else:
        return render(request,"login.html",{'msg':"Wrong Userid Or Password"})


def paswordAuto(request):
    try:
        idn=MerchantModel.objects.all()[::-1][0]
        idno=int(idn.merchant_id)+1
    except:
        idno=17850

    password=600000
    return render(request,"addmerchant.html",{'password':password,'idno':idno})


def savemerchant(request):
    idno=request.POST['idn']
    name=request.POST['mcna']
    contact=request.POST['cont']
    email=request.POST['eml']
    pssd=email[0]+contact[-1]+str(len(name)+int(idno))+contact[0]+email[1]+email[2]
    print(pssd)


    try:
        MerchantModel(merchant_id=idno,name=name,contact_no=contact,password=pssd,email_id=email).save()
        return render(request,"index.html",{'data':'Saved Sucessfully'})
    except:
        return render(request,"addmerchant.html",{"dupmsg":"Merchant already Registered"})


def viewmerchant(request):
    return render(request,"index.html",{'data2':MerchantModel.objects.all()})


def delte(request):
    idno=request.POST['del']
    MerchantModel.objects.get(merchant_id=idno).delete()
    return render(request,"index.html",{'delmsg':'Deletd SucessFully'})


class CheckPassword(View):
    def get(self,request,uid,upass):
        try:
            res=MerchantModel.objects.get(email_id=uid,password=upass)
        except:
            data=json.dumps({'msg':'Invalid'})
            return HttpResponse(data,content_type="application/json",status=400)
        else:
            data = serialize('json',[res])
            return HttpResponse(data, content_type="application/json", status=200)


@method_decorator(csrf_exempt,name='dispatch')
class ChangePsd(View):
    def put(self,request,emailid):
        d1=request.body
        new_dict=json.loads(d1)

        try:
            res=MerchantModel.objects.get(email_id=emailid)
            old_pass={'merchant_id':res.merchant_id,
                      'name':res.name,
                      'password':res.password,
                      'contact_no':res.contact_no,
                      'email_id':res.email_id}
        except:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)
        else:
            old_pass.update(new_dict)
            merchantform=MerchantForm(old_pass,instance=res)
            if merchantform.is_valid():
                merchantform.save()
            data = json.dumps({'msg': 'valid'})
            return HttpResponse(data, content_type="application/json", status=200)


@method_decorator(csrf_exempt,name='dispatch')
class Addproduct(View):
    def post(self,request):
        data=request.body
        product_data=json.loads(data)
        productform=ProductForm(product_data)
        if productform.is_valid():
            productform.save()
            data = json.dumps({'msg': 'valid'})
            return HttpResponse(data,content_type="application/json",status=200)
        else:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)


class SendProduct(View):
    def get(self,request,mer_id):
        try:
            status=ProductModel.objects.filter(merchant_id=mer_id)
        except:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)
        else:
            data = serialize('json',status)
            return HttpResponse(data, content_type="application/json", status=200)




@method_decorator(csrf_exempt,name='dispatch')
class SendOneProduct(View):
    def delete(self,request,product_id):
        try:
            ProductModel.objects.get(product_no=product_id).delete()
            data = json.dumps({'msg': 'valid'})
            return HttpResponse(data, content_type="application/json", status=200)
        except:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)


    def get(self,request,product_id):
        try:
            res=ProductModel.objects.get(product_no=product_id)
        except:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)
        else:
            data = serialize('json', [res])
            return HttpResponse(data, content_type="application/json", status=200)
    def put(self,request,product_id):
        d1=request.body
        new_data=json.loads(d1)
        try:
            res=ProductModel.objects.get(product_no=product_id)
            old_data={'product_no': res.product_no,
                     'name': res.name,
                     'price': res.price,
                     'quantity': res.quantity,
                     'merchant': res.merchant}
        except:
            data = json.dumps({'msg': 'Invalid'})
            return HttpResponse(data, content_type="application/json", status=400)
        else:
            old_data.update(new_data)
            productform=ProductForm(old_data,instance=res)
            if productform.is_valid():
                productform.save()
                data = json.dumps({'msg': 'Invalid'})
                return HttpResponse(data, content_type="application/json", status=200)
            else:
                data = json.dumps({'msg': 'Invalid'})
                return HttpResponse(data, content_type="application/json", status=400)

