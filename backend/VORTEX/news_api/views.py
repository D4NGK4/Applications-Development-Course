from django.shortcuts import render

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newsapi import NewsApiClient
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import NewsSerializer

import environ
from pathlib import Path

env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / "../.env")

newsapi = NewsApiClient(api_key=env("NEWSAPIKEY"))

class TopNewsAPIView(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        q = request.query_params.get('q', None)
        category = request.query_params.get('category', None)
        language = request.query_params.get('language', None)
        country = request.query_params.get('country', None)
        
        top_headlines = newsapi.get_top_headlines(q=q, category=category, language=language, country=country)
        articles = top_headlines.get('articles', [])
        serializer = NewsSerializer({'articles': articles})
        return Response(serializer.data, status=status.HTTP_200_OK)

class EverythingNewsAPIView(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        q = request.query_params.get('q', None)
        language = request.query_params.get('language', None)
        
        all_articles = newsapi.get_everything(q=q, language=language)
        articles = all_articles.get('articles', [])
        serializer = NewsSerializer({'articles': articles})
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.

# Create your views here.
