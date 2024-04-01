from django.urls import path
from car import views

urlpatterns = [
    path('', views.SelectAnimalView.as_view(), name="SelectAllAnimal"),
    path('<int:pk>', views.SelecAnimalView.as_view(), name="SelectOneAnimal"),
    path('add', views.AddAnimalView.as_view(), name="AddCars"),
    path('dlete/<int:pk>', views.DeleteAnimalView.as_view(), name="DeleteAnimal"),


]