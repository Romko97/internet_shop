from django.urls import path
from . import views, utils

urlpatterns = [
    path('', views.store, name='store'),
    path('Login/', views.Login, name='Login'),
    path('signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path("<int:pk>/", views.detailView, name="detailView"),

]