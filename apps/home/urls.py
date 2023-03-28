# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('client/list/', views.client_list, name='client_list'),
    path('client/info/<int:pk>/', views.client_info, name='client_info'),

    path('cotisation/list/', views.cotisation_list, name='cotisation_list'),
    path('cotisation/info/<int:pk>/', views.cotisation_info, name='cotisation_info'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
