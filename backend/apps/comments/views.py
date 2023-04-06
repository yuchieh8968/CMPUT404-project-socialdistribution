from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Comment
from apps.authors.models import Author
from django.http import Http404
from .serializers import CommentSerializer, CommentPostSerializer
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


class CommentView(GenericAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, author_id, post_id):
        # Filtering the query to get likes
        try:
            query_obj = Comment.objects.filter(
                author__id=author_id, post__id=post_id)
            return query_obj
        except:
            raise Http404

    def get(self, request, author_id, post_id, format=None):
        obj = self.get_object(author_id, post_id)
        serializer = CommentSerializer(obj, many=True)
        return Response({
            "type": "comments",
            "post": f"http://127.0.0.1:5454/authors/{author_id}/posts/{post_id}",
            "id": f"http://127.0.0.1:5454/authors/{author_id}/posts/{post_id}/comments",
            "comments": serializer.data
        })

    def post(self, request, author_id, post_id):
        """
        URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments
        POST [local] if you post an object of “type”:”comment”, it will add your comment to the post whose id is POST_ID
        """

        request.data['post_id'] = post_id
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
