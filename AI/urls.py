from django.urls import path, include

from .views import AiAPIView

urlpatterns = [
    path('chat/', AiAPIView.as_view(), name='ai_chat')
]