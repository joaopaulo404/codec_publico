
#Quando um cliente enviar uma requisição usando um HTTP Request (GET, POST, PUT ou DELETE), as views definirão como o servidor vai responder definindo as rotas
from django.urls import re_path
from API_LOCALIDADES import views 
 
urlpatterns = [ 
    re_path(r'^api/municipios$', views.getCidades, name='getCidades'),
    re_path(r'^api/bairros$', views.getBairros, name='getBairros'),

]
