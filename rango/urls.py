from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('scenery/', views.about, name='about'),
    path('city/<slug:city_name_slug>/', views.show_scenery, name='show_scenery'),
    path('add_city/', views.add_city, name='add_city'),
    path('city/<slug:city_name_slug>/add_scenery/', views.add_scenery, name='add_scenery'),
    path('mypage/', views.mypage, name='mypage'),
]