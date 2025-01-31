from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('home/', views.index, name = 'home'),
    path('exercises/', views.exercises, name = 'exercises'),
    path('chest/', views.chest, name = 'chest'),
    path('back/', views.back, name = 'back'),
    path('bicep/', views.bicep, name = 'bicep'),
    path('tricep/', views.tricep, name = 'tricep'),
    path('shoulder/', views.shoulder, name = 'shoulder'),
    path('legs/', views.legs, name = 'legs'),
    path('abs/', views.abs, name = 'abs'),
    path('membership/', views.membership, name = 'membership'),
    path("registration", views.registration, name = 'registration'),
    path('chest1/', views.chest1, name = 'chest1'),
    path('chest2/', views.chest2, name = 'chest2'),
    path('chest3/', views.chest3, name = 'chest3'),
    path('chest4/', views.chest4, name = 'chest4'),
    path('chest5/', views.chest5, name = 'chest5'),
    path('chest6/', views.chest6, name = 'chest6'),
    path('chest7/', views.chest7, name = 'chest7'),
    path('chest8/', views.chest8, name = 'chest8'),
    path('chest9/', views.chest9, name = 'chest9'),
    path('chest10/', views.chest10, name = 'chest10'),
]