from django.urls import path
from . import views

namespace='products'
urlpatterns = [
    path('',views.productcategory,name='productcat'),
    path('<slug:slug>/', views.products, name='products'),
]