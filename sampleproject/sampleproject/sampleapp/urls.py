
from django.urls import path

from sampleapp import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('',views.demo,name='res')

]
