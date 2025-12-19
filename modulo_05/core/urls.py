from django.urls import path
from .views import (
    ListaTarefasAPIView,
    DetalheTarefaAPIView,
    MeView,
    ChangePasswordView,
    UserStatsAPIView,
)

app_name = "core"

urlpatterns = [
    path("tarefas/", ListaTarefasAPIView.as_view(), name="lista-tarefas"),
    path("tarefas/<int:pk>/", DetalheTarefaAPIView.as_view(), name="detalhe-tarefa"),
    path("me/", MeView.as_view(), name="me"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("stats/", UserStatsAPIView.as_view(), name="user-stats"),
]
