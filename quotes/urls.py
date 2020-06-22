from django.urls import path
from . import views	

urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('about/',views.about,name='about'),
    path('add_stock/',views.add_stock,name='add_stock'),

]