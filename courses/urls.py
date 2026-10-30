from django.urls import path
from .views import get_hello, post, query, patch, safe_query, ItemAPIView

urlpatterns = [
    path('hel/', get_hello, name='hello'), 
    path('post/', post, name='post'),
    path('q/', query, name='query'),
    path('patch/<str:name>/', patch, name='patch'),
    path('sq/', safe_query, name='safe_query'),
    path('vi/<int:item_id>/', ItemAPIView.as_view()),
    path('vi/', ItemAPIView.as_view()),
]