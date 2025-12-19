from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from django.db import IntegrityError
from django.utils import timezone
from .models import Tarefa
from .serializers import TarefaSerializer, UserProfileSerializer
from .permissions import IsAdminOrOwner
import logging

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            # Admin vê tudo
            return Tarefa.objects.filter(deletada=False)

        return Tarefa.objects.filter(user=user, deletada=False)

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = TarefaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(
                data=request.data, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "Erro interno."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


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
