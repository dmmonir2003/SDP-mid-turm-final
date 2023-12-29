from django.urls import path
from . import views

urlpatterns = [
    
    path('brand/<slug:brand_name>/',views.BrandCarListView.as_view(), name='brand_cars'),
    path('',views.HomePage.as_view(),name='home_page'),
    # path('brand_car/<slug:brand_name>/',views.brand_car.as_view(),name='brand_car'),
    path('details/<int:pk>',views.details.as_view(),name='details_car'),
    path('buy_car/<int:id>', views.buy_car, name='buy_car'),
]