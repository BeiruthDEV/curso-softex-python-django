from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from .models import Tarefa
from .serializers import TarefaSerializer, UserProfileSerializer
from .permissions import (
    IsAdminOrOwner,
)


class ListaTarefasAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Tarefa.objects.filter(deletada=False)
        return Tarefa.objects.filter(user=user, deletada=False)

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = TarefaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TarefaSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalheTarefaAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_object(self, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk, deletada=False)
        self.check_object_permissions(self.request, tarefa)
        return tarefa

    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(
            tarefa, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.deletada = True
        tarefa.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not user.check_password(old_password):
            return Response({"error": "Senha atual incorreta"}, status=400)
        user.set_password(new_password)
        user.save()
        return Response({"detail": "Senha alterada com sucesso"})


class UserStatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Tarefa.objects.filter(user=request.user, deletada=False)
        stats = queryset.aggregate(
            total=Count("id"), concluidas=Count("id", filter=Q(concluida=True))
        )
        total = stats["total"] or 0
        concluidas = stats["concluidas"] or 0
        pendentes = total - concluidas
        taxa = (concluidas / total) if total > 0 else 0
        return Response(
            {
                "total_tarefas": total,
                "concluidas": concluidas,
                "pendentes": pendentes,
                "taxa_conclusao": round(taxa, 2),
            }
        )


class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
            }
        )
    
    user = serializers.StringRelatedField(read_only=True)
class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id', 'user', 'criada_em']
        

def validate_titulo(self, value):
        """
        Validação customizada para o campo 'titulo'.
        Regras:
        - Não pode ser vazio (após strip)
        - Não pode conter apenas números
        - Deve ter pelo menos 3 caracteres
        """
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )

        
        return value