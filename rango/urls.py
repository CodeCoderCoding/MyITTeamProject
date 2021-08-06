from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('city/<slug:city_name_slug>/', views.show_scenery, name='show_scenery'),
    path('mycity/<slug:city_name_slug>/', views.show_my_scenery, name='show_my_scenery'),
    path('add_city/<slug:user_name_slug>/', views.add_city, name='add_city'),
    path('add_scenery/<slug:city_name_slug>/<slug:user_name_slug>/', views.add_scenery, name='add_scenery'),
    path('mypage/<slug:user_name_slug>/', views.mypage, name='mypage'),
]