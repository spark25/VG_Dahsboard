from django.urls import path

from . import views

urlpatterns = [
    path('sli/', views.sli_dash, name='sli_dash'),
    path('sli/reg_focus', views.sli_reg_focus, name='sli_reg_focus'),
    path('kr/', views.kr_dash, name='kr_dash'),
]