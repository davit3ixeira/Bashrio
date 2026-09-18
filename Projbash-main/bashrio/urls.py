from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_view, name="login"),
  path('processar-login/', views.processar_login, name="processar_login"),
  path('cadastro/', views.cadastro, name="cadastro"),
  path('logout/', views.logout_view, name="logout"),
  path('home/', views.home, name="home"),
  path('alterar-senha/', views.alterar_senha, name="altera_senha"),
  path('esqueci-senha/', views.esqueci_senha, name="esqueci_senha"),
  path('add-eventos/', views.addEventos, name="add_eventos"),
  path('cadastrar-evento/', views.cadastrar_evento, name="cadastrar_evento"),
  path('inicio-conta/', views.inicio_conta, name="inicio_conta"),
]