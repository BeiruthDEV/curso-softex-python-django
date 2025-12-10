from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from django.db import IntegrityError
from django.utils import timezone
from .models import Tarefa
from .serializers import TarefaSerializer
import logging

logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        queryset = Tarefa.objects.filter(deletada=False)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        serializer = TarefaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'error': 'Violação de integridade.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response({'error': 'Erro interno.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetalheTarefaAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk, deletada=False)

    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.deletada = True
        tarefa.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstatisticasTarefaAPIView(APIView):
    def get(self, request):
        stats = Tarefa.objects.filter(deletada=False).aggregate(
            total=Count('id'),
            concluidas=Count('id', filter=Q(concluida=True))
        )
        total = stats['total'] or 0
        concluidas = stats['concluidas'] or 0
        pendentes = total - concluidas
        taxa = (concluidas / total) if total > 0 else 0
        
        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa, 2)
        }, status=status.HTTP_200_OK)

class DuplicarTarefaAPIView(APIView):
    def post(self, request, pk, format=None):
        tarefa_original = get_object_or_404(Tarefa, pk=pk, deletada=False)
        
        tarefa_original.pk = None
        tarefa_original.titulo = f"{tarefa_original.titulo} (Cópia)"
        tarefa_original.concluida = False
        tarefa_original.data_conclusao = None
        tarefa_original.criada_em = timezone.now()
        tarefa_original.save()
        
        serializer = TarefaSerializer(tarefa_original)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConcluirTodasTarefasAPIView(APIView):
    def patch(self, request, format=None):
        user_id = request.data.get('user_id')
        
        queryset = Tarefa.objects.filter(concluida=False, deletada=False)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        
        count = queryset.update(concluida=True, data_conclusao=timezone.now())
        
        return Response({
            "mensagem": f"{count} tarefas foram concluídas com sucesso."
        }, status=status.HTTP_200_OK)