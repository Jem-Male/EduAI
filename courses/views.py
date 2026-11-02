from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


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


class CourseAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            return Response({"info": "Not parametrs"}, status=status.HTTP_400_BAD_REQUEST)
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonAPIViews(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer