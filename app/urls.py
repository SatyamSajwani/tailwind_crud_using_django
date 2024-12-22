from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name='home'),
    path('update',views.update,name='update'),
    path('login',views.login,name='login'),
    path('ragister',views.ragister,name='ragister'),
]
