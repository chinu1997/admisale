from django.shortcuts import render
from Admin.models import ProductModel,CoustemerModel
# Create your views here.
def Showproduct(request):
    productdata=ProductModel.objects.all()
    return render(request,"coustemer/coustemerindex.html",{'data':productdata})


def CoustemerRegistration(request):
    cname=request.POST['can']
    contact=request.POST['cont']
    address=request.POST['adds']
    email=request.POST['eml']
    password=request.POST['pssd']
    try:
        CoustemerModel(name=cname,contact=contact,address=address,email=email,password=password).save()
        return render(request,"coustemer/coustemerindex.html",{'sucsmsg':'DataSaved SucessFully'})
    except:
        return render(request,"coustemer/registration.html",{'ermsg':'You Are Already exist'})


def CoustemerloginCheck(request):
    return render(request,"coustemer/coslogin.html")


def CheckLogin(request):
    email=request.POST['eml']
    passd=request.POST['psd']
    if '@' in email:
        try:
            res=CoustemerModel.objects.get(email=email,password=passd)
            productdata = ProductModel.objects.all()
            return render(request, "coustemer/LoginSucess.html", {'data': productdata})

        except:
            return render(request,"coustemer/coslogin.html",{'data':"Wrong UserId Or Password"})
    else:
        try:
            res=CoustemerModel.objects.get(contact=email,password=passd)
            productdata = ProductModel.objects.all()
            return render(request, "coustemer/LoginSucess.html", {'data': productdata})

        except:
            return render(request, "coustemer/coslogin.html", {'data': "Wrong UserId Or Password"})
