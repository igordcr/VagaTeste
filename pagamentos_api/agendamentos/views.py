from rest_framework import generics
from .models import Agendamento
from .serializers import AgendamentoSerializer

class AgendamentoCreate(generics.CreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class AgendamentoList(generics.ListAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class AgendamentoDetail(generics.RetrieveAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class AgendamentoDelete(generics.DestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


from django.http import HttpResponse
def home(request):
    return HttpResponse("Bem-vindo à API de Agendamentos!")