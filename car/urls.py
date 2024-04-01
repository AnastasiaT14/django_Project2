from django.urls import path
from car import views

urlpatterns = [
    path('', views.SelectCarView.as_view(), name="SelectAllCars"),
    path('<int:pk>', views.SelectCarView.as_view(), name="SelectOneCars"),
    path('add', views.AddCarView.as_view(), name="AddCars"),
    path('dlete/<int:pk>', views.DeleteCarView.as_view(), name="DeleteCars"),


]