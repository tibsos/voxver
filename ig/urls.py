from django.urls import path

from .views import *

app_name = 'ig'

urlpatterns = [

    path('', page, name = 'page'),

]