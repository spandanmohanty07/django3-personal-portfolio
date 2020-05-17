from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')
] 
