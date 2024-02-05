from django.urls import path
from api_v2.views import json_echo_view, get_token_view, ArticleView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView

app_name = 'api_v2'

urlpatterns = [
    path('echo/', json_echo_view, name='echo'),
    path('token/', get_token_view, name='get_token'),
    path('article/', ArticleView.as_view(), name='article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete')
]
