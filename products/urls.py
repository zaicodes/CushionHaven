from django.urls import path
from . import views
urlpatterns = [
    path('', views.allproducts, name="products"),

]
