from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from serializers import LessonSerializer


@api_view(['GET'])
def get_hello(request):
    return Response({"mes":"Hello!"}, status=status.HTTP_226_IM_USED)


@api_view(['POST'])
def post(request):
    return Response(request.data)


@api_view(['GET', 'POST'])
def query(request):
    if request.method == 'GET':
        return Response({"info":"Send post query parametrs"})
    data = request.query_params
    return Response(data)


@api_view(['GET'])
def safe_query(request):
    a = request.query_params.get('name', 'default')
    data = request.query_params
    return Response({
        "name": a,
        "other query": data
    })


@api_view(['GET'])
def patch(request, name):
    return Response(name)


class ItemAPIView(APIView):
    def get(self, request, item_id=None):
        if item_id is None:
            return Response({"info": "Not parametrs"})
        return Response({
            "data": f"Item - {item_id}"
        })
    
    
    def post(self, request):    
        serializer = LessonSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        
        serializer.save()
        return Response(
            {
                "status":"sucess",
                "result": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

