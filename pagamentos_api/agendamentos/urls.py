from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.AgendamentoList.as_view(), name='agendamento-list'),
    path('agendamentos/<int:pk>/', views.AgendamentoDetail.as_view(), name='agendamento-detail'),
    path('agendamentos/create/', views.AgendamentoCreate.as_view(), name='agendamento-create'),
    path('agendamentos/<int:pk>/delete/', views.AgendamentoDelete.as_view(), name='agendamento-delete'),
    ##
    ##path('', views.home, name='home'),  ## Página inicial
    
]

