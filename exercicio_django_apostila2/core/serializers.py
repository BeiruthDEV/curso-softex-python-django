from rest_framework import serializers
from .models import Tarefa
from datetime import date


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ["id", "titulo", "concluida", "prioridade", "prazo", "criada_em"]
        read_only_fields = ["id", "criada_em"]

    def validate_titulo(self, value):
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

    def validate_prazo(self, value):
        if value and value < date.today():
            raise serializers.ValidationError(
                "O prazo não pode ser uma data no passado."
            )
        return value

    def validate(self, data):
        # Recupera valores (seguro contra atualizações parciais)
        concluida = data.get("concluida", False)
        prazo = data.get("prazo")

        if not concluida and not prazo:
            raise serializers.ValidationError(
                {"prazo": "Para tarefas pendentes, o prazo é obrigatório."}
            )

        return data
