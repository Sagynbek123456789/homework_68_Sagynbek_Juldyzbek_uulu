import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from webapp.models import Article
from api_v2.serializers import ArticleSerializer, ArticleModelSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.
@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def json_echo_view(request, *args, **kwargs):
    answer = {
        'massage': 'Hello word',
        'method': request.method
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    return JsonResponse(answer)


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleView(APIView):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('-created_at')
        articles_list = ArticleModelSerializer(articles, many=True).data
        return Response(articles_list)

    def post(self, request, *args, **kwargs):
        serializer = ArticleModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ArticleModelSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        return Response({'id': instance_id})
