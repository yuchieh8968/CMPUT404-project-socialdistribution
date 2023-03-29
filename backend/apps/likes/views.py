from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Like
from apps.authors.models import Author
from django.http import Http404
from .serializers import LikeSerializer
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from urllib.parse import unquote, quote
from datetime import datetime
import uuid
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from apps.authors.remoteauth import RemoteAuth
from django.shortcuts import render
from django.template import loader
import requests
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas.openapi import AutoSchema
from django.conf import settings

# Create your views here.
class Post_A_Like(GenericAPIView):
    serializer_class = LikeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request, author_id, format=None):
        """
        URL: ://service/authors/{AUTHOR_ID}/inbox/
        POST [local, remote]: send a like object to AUTHOR_ID
        """
        
        serializer = LikeSerializer(Like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Get_Like_For_Post(GenericAPIView):
    serializer_class = LikeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, author_id, post_id):
        # Filtering the query to get likes 
        try:
            query_obj = Like.objects.filter(author=author_id)
            query_obj2 = query_obj.filter(object__icontains=str(f'/posts/{post_id}'))
            return query_obj2
        except:
            raise Http404
    
    def get(self, request, author_id, post_id, format=None):
        """
        URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/likes
        GET [local, remote] a list of likes from other authors on AUTHOR_ID’s post POST_ID
        """
        obj = self.get_object(author_id, post_id)
        serializer = LikeSerializer(obj)
        return Response(serializer.data)