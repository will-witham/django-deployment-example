from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('index/', views.index, name='index'),
    path('user_login',views.user_login, name='user_login'),
    path('special',views.special,name='special')
]
