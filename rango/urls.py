from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('scenery/', views.about, name='about'),
    path('city/<slug:city_name_slug>/', views.show_scenery, name='show_scenery'),
    path('add_city/', views.add_city, name='add_city'),
    path('city/<slug:city_name_slug>/add_scenery/', views.add_scenery, name='add_scenery'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    # path('logout/', views.user_logout, name='logout'),
]