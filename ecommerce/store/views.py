from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from . utils import *


def store(request):
    
     data = cartData(request)
     cartItems = data['cartItems'] 

     products = Product.objects.all()
     context = {'products':products, 'cartItems':cartItems}
     return render(request, 'store/store.html', context)


def cart(request):
   
     data = cartData(request)
     cartItems = data['cartItems']
     order = data['order']
     items = data['items']
          
     context = {'items':items, 'order':order, 'cartItems':cartItems}
     return render(request, 'store/cart.html', context)


def checkout(request):

     data = cartData(request)
     cartItems = data['cartItems']
     order = data['order']
     items = data['items']
     # """""""""""""""""OLD CODE"""""""""""""""""
     # items = []
     # order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
     # cartItems = order['get_cart_items']

     context = {'items':items, 'order':order, 'cartItems':cartItems}
     return render(request, 'store/checkout.html', context)


def updateItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']
     
     print('Action:', action)
     print('productId:', productId)

     customer = request.user.customer
     product = Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer, complete=False)
     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
     if action == 'add':
          orderItem.quantity = (orderItem.quantity + 1)
     elif action == 'remove':
          orderItem.quantity = (orderItem.quantity - 1)
     orderItem.save()
     if orderItem.quantity <= 0:
          orderItem.delete()
     

     return JsonResponse('Item was added', safe=False)


def processOrder(request):
     transaction_id = datetime.datetime.now().timestamp()
     data = json.loads(request.body)

     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
         

         

     else:
          customer, order = guestOrder(request, data)
          

     total = float(data['form']['total'])
     order.transaction_id = transaction_id

     if total == order.get_cart_total:
          order.complete = True
     order.save()

     if order.shipping == True:
          ShippingAdress.objects.create(
               customer=customer,
               order=order,
               address=data['shipping']['address'],
               city=data['shipping']['city'],
               state=data['shipping']['state'],
               zipcode=data['shipping']['zipcode'],
          )

     return JsonResponse('Payment complete', safe=False)

# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['romanhalychanivskyi@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     print("fuck you")
#     return render(request, 'store/checkout.html')
    

def detailView(request, pk):
     data = cartData(request)
     cartItems = data['cartItems']
     product = Product.objects.get(pk=pk)
     context = {'product':product, 'cartItems':cartItems}
     print("fuck you")
     return render(request, 'store/detailView.html', context)
