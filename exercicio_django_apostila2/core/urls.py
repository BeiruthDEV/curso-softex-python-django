# Exercicio 3
from django.urls import path
from .views import ListaTarefasAPIView, EstatisticasTarefaAPIView

urlpatterns = [
    path("tarefas/", ListaTarefasAPIView.as_view(), name="lista-tarefas"),
    path(
        "tarefas/estatisticas/",
        EstatisticasTarefaAPIView.as_view(),
        name="estatisticas-tarefas",
    ),
]
