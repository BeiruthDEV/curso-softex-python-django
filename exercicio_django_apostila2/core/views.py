# Exercicio 3
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q
from .models import Tarefa
from .serializers import TarefaSerializer

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(
                    f"Tarefa criada com sucesso: ID {serializer.data.get('id')}"
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            logger.warning(f"Falha na validação: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Erro interno ao criar tarefa: {str(e)}")
            return Response(
                {"error": "Erro interno do servidor."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EstatisticasTarefaAPIView(APIView):

    def get(self, request, format=None):
        stats = Tarefa.objects.aggregate(
            total=Count("id"), concluidas=Count("id", filter=Q(concluida=True))
        )

        total = stats["total"] or 0
        concluidas = stats["concluidas"] or 0
        pendentes = total - concluidas

        taxa = (concluidas / total) if total > 0 else 0

        return Response(
            {
                "total": total,
                "concluidas": concluidas,
                "pendentes": pendentes,
                "taxa_conclusao": round(taxa, 2),
            }
        )
