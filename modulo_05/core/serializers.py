from rest_framework import serializers
from django.utils import timezone
from .models import Tarefa
from datetime import date

class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
        }
    )

    class Meta:
        model = Tarefa
        fields = [
            'id', 'user', 'titulo', 'descricao', 
            'concluida', 'data_conclusao', 'prioridade', 
            'prazo', 'deletada', 'criada_em'
        ]
        read_only_fields = ['id', 'criada_em', 'data_conclusao']

    def validate_titulo(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("O título não pode ser vazio.")
        if len(value) < 3:
            raise serializers.ValidationError("O título deve ter pelo menos 3 caracteres.")
        if value.isdigit():
            raise serializers.ValidationError("O título não pode conter apenas números.")
        return value

    def validate_prazo(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("O prazo não pode ser uma data no passado.")
        return value

    def validate(self, data):
        concluida_no_request = data.get('concluida')
        concluida_atual = self.instance.concluida if self.instance else False
        
        esta_concluida = concluida_no_request if concluida_no_request is not None else concluida_atual

        prazo = data.get('prazo')
        tem_prazo = prazo is not None or (self.instance and self.instance.prazo)

        if not esta_concluida and not tem_prazo:
             if not self.instance or not self.instance.prazo:
                raise serializers.ValidationError({"prazo": "O prazo é obrigatório para tarefas pendentes."})

        if self.instance and self.instance.prioridade == 'alta':
            if concluida_no_request is True and not concluida_atual:
                request = self.context.get('request')
                if request and request.method == 'PATCH':
                    raise serializers.ValidationError(
                        "Tarefas de alta prioridade só podem ser concluídas via PUT (edição completa)."
                    )

        return data

    def update(self, instance, validated_data):
        concluida_anterior = instance.concluida
        concluida_nova = validated_data.get('concluida', concluida_anterior)

        if not concluida_anterior and concluida_nova:
            instance.data_conclusao = timezone.now()
        
        elif concluida_anterior and not concluida_nova:
            instance.data_conclusao = None

        return super().update(instance, validated_data)