
#Quando um cliente enviar uma requisição usando um HTTP Request (GET, POST, PUT ou DELETE), as views definirão como o servidor vai responder definindo as rotas
from django.urls import re_path
from API_CONSOLIDADOS import views 
 
urlpatterns = [ 
    re_path(r'^api/consolidados$', views.getConsolidados, name='getConsolidados'),
    re_path(r'^api/cvli/(?P<mes_fato>[\w_-]+)/$', views.getCVLI, name='getCVLI'),

]