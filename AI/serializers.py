from rest_framework import serializers

from .models import AiInstruction


class InstructionSerializer(serializers.Serializer):
    class Meta:
        model = AiInstruction
        fields = ['__all__']


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()