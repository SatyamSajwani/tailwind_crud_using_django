from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('ragister',views.register ,name='ragister'),
    path('',views.home ,name='mainhome'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('insert/',views.insert,name='insert'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('home',views.index,name='home'),
=======
    path('',views.index ,name='home'),
    path('update',views.update,name='update'),
    path('login',views.login,name='login'),
    path('ragister',views.ragister,name='ragister'),
    path('create',views.create,name='create'),
>>>>>>> 66b2e2d5c4707e87983c65d3d5d978dfe906c7ef
]
