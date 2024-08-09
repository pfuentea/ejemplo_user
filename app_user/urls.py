from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='home'),
    path('update_profile/',views.profile,name='update_profile'),
    path('new_propiedad/',views.crear_prop,name='new_propiedad'),
]