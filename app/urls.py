
from django.urls import path,include
from .views import home,delete_data,form_data,edit

urlpatterns = [
    
    path("",home,name="home"),
    path("<int:id>/delete/",delete_data,name="delete"),
    path('form/',form_data,name="form"),
    path("edit/<int:id>",edit,name="edit")
    
]