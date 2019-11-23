from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path('about/',views.about,name="About Us"),
    path('contact/',views.contact,name="contact Us"),
    path('tracker/',views.tracker,name="trackingStatus"),
    path('products/<int:myid>',views.prodview,name="productView"),
    path('search/',views.search,name="Search"),
    path('checkout/',views.checkout,name="Checkout"),
]
