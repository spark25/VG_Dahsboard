from django.urls import path

from . import views

urlpatterns = [
    path('sli/', views.sli_dash, name='sli_dash'),
]