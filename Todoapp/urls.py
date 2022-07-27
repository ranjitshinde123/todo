from django.contrib import admin

from django.contrib import admin
from django.urls import path,include
from .views import home,login,signup,add_todo,signout,delete_todo,change_todo
from . import views

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup),
    path('add_todo/',add_todo),
    path('delete_todo/<int:id>',delete_todo),
    path('change_status/<int:id>/<str:status>',change_todo),
    path('logout/', signout),
 ]