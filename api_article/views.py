from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_article.models import Article
from api_article.serializers import ArticleSerializer
from django.shortcuts import get_object_or_404

# 강력한놈
from rest_framework import generics

# 클래스기반에 권한 부여
from rest_framework.permissions import IsAuthenticated
permission_classes = [IsAuthenticated]


# @api_view(['GET', 'POST'])
# def article_list(request, format=None):
#     """
#     List all articles, or create a new article
#     """
#     if request.method == 'GET':
#         articles = Article.objects.all()

#         articles_serializer = ArticleSerializer(articles, many=True)
#         return Response(articles_serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         article_serializer = ArticleSerializer(data=request.data)
#         if article_serializer.is_valid():
#             article_serializer.save()
#             print('New Article Made!')
#             return Response(article_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a article
#     """
#     try:
#         article = get_object_or_404(Article, pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'GET':
#         article_serializer = ArticleSerializer(article)
#         return Response(article_serializer.data)
    
#     elif request.method == 'PUT':
#         article_serializer = ArticleSerializer(article, request.data)
#         if article_serializer.is_valid():
#             article_serializer.save()
#             return Response(article_serializer.data, status=status.HTTP_200_OK)
#         return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

