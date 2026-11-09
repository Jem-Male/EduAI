from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer

from .chat import AI

class AiAPIView(APIView):
    def get(self, request):
        return Response({
            "POST": {
                "message": 'input message'
            }
        })
    
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = AI.get_chat_response(serializer.validated_data['message']) # type: ignore
        return Response(response)