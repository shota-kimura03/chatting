from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexfunc, name='index'),
    path('list/', views.listfunc, name='list'),
    path('login/', views.loginfunc, name='login'),
    path('signup/', views.signupfunc, name='signup'),
    path('<slug:room_name1>/<slug:room_name2>/', views.roomfunc, name='room'),
]