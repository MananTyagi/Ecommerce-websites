from django.shortcuts import render, HttpResponse
from shop.models import Product, Contact, Order, OrderUpdate
import math
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

# Create your views here.
def index(request):
    # allproducts= Product.objects.all()
    # n= len(allproducts)
    # no_of_slides= n//4 + math.ceil((n/4)-(n//4))
    # context={"all":allproducts,"nsl":no_of_slides,"range":range(1,no_of_slides+1)}
    allprods=[]
    catprods=Product.objects.values("category",'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n= len(prod)
        no_of_slides= n//4 + math.ceil((n/4)-(n//4))
        allprods.append([prod,range(1,no_of_slides), no_of_slides])
    # allprods=[[allproducts, range(1,no_of_slides),no_of_slides], [allproducts, range(1,no_of_slides),no_of_slides]]
    context={'allProds':allprods}
    return render(request,'shop/index.html',context)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name= request.POST.get("name",'')
        email= request.POST.get("email",'')
        desc= request.POST.get("prob",'')
        order=Contact(name=name, email=email, desc=desc)
        order.save()
    return render(request,'shop/contact.html')
def tracker(request):
    response = None
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
  
    if request.method=="POST":
        name= request.POST.get("name",'')
        items=request.POST.get("itemsjson",'')
        amount = request.POST.get('amount', '')
        email= request.POST.get("email",'')
        phone= request.POST.get("phone",'')
        address= request.POST.get("add1",'')+" "+request.POST.get("add2",'')
        city= request.POST.get("city",'')
        zip_code= request.POST.get("zip_code",'')
        state= request.POST.get("state",'')
        phone= request.POST.get("phone",'')
       
        order=Order(name=name,items_json=items, email=email,  state=state, phone=phone, address=address, city=city, zip_code=zip_code,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        global id
        id=order.getid()
        print(id)
    param_dict={

            'MID': 'WorldP64425807474247',
            'ORDER_ID': 'order.order_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlepayment/',

    }
    return  render(request, 'shop/paytm.html', {'param_dict': param_dict})
    return render(request, 'shop/checkout.html')
    #return render(request,'shop/checkout.html',{'id':id})
def productview(request, myid):
    
    singleprod= Product.objects.filter(id=myid)
    print(singleprod)
    return render(request,'shop/productview.html',{"singleprod":singleprod[0]})

@csrf_exempt
def handle_request(request):
    pass