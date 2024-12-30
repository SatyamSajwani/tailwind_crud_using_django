from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ragister',views.register ,name='ragister'),
    path('',views.home ,name='mainhome'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('insert/',views.insert,name='insert'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('home',views.index,name='home'),
]
