from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/<username>/', views.user, name='user'),
    path('services/<service_name>/', views.service, name='service'),
    path('all/<username>/<service_name>/',
         views.user_service, name='user_service'),
    path('new', views.create, name='new_media_object'),
]
