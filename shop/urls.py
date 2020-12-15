from django.urls import path
from . import views
urlpatterns = [

    path('', views.index,name="shophome",),
    path('about/', views.about,name="about",),
    path('contact/', views.contact,name="contact",),
    path('tracker/', views.tracker,name="tracker",),
    path('productview/<int:myid>', views.productview,name="productview",),
    path('search/', views.search,name="seach",),
    path('checkout/', views.checkout,name="checkout",),
    path('handle_request/', views.handle_request,name="handle_request"),
]