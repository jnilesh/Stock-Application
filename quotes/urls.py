from django.urls import path
from . import views	

urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('about/',views.about,name='about'),
    path('add_stock/',views.add_stock,name='add_stock'),
    path('delete_ticker/<str:symbol>/',views.delete_ticker,name='delete_ticker'),
    path('detail_view/<str:symbol>/',views.detail_view,name='detail_view'),

]
