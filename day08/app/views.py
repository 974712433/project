from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()

    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclasss = shops[3:7]
    shopcommends = shops[7:11]

    mainshows = MainShow.objects.all()

    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclasss':shopclasss,
        'shopcommends':shopcommends,
        'mainshows':mainshows,
    }
    return render(request,'home/home.html',context=data)



def cart(request):
    return render(request,'cart/cart.html')


def market(request):
    return render(request,'market/market.html')


def mine(request):
    return render(request,'mine/mine.html')