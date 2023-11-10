
from django.urls import re_path, path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download_recorte', views.download_recorte, name='download_recorte'),
    path('analise', views.analise, name="analise"),

]