from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("background_investigation/", views.background_investigation, name='background_investigation'),
    path("product_design/", views.product_design, name='product_design'),
    path("continuous_meaning/", views.continuous_meaning, name='continuous_meaning'),
    path("tech_support/", views.tech_support, name='tech_support'),
    path('homework_echarts/', views.homework_echarts, name='homework_echarts'),
    path('product_echarts/', views.product_echarts, name='product_echarts')
]
