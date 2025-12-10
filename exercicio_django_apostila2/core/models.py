"""
Exercicio 1 e 2
"""

from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    concluida = models.BooleanField(default=False, verbose_name="Concluída")
    criada_em = models.DateTimeField(auto_now_add=True, verbose_name="Criada em")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuário"
    )

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default="media",
        verbose_name="Prioridade",
    )

    prazo = models.DateField(null=True, blank=True, verbose_name="Prazo de Conclusão")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["-criada_em"]

    def __str__(self):
        return f"{self.titulo} - {self.get_prioridade_display()}"
