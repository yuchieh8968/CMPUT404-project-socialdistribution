from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Post
from apps.authors.models import Author
from django.http import Http404
from .serializers import PostSerializer
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
from apps.authors.remoteauth import RemoteAuth
from django.shortcuts import render
from django.template import loader
import requests
import json



# Create your views here.

# def GuiPost(request, author_text, post_text):
def GuiPost(request):
    

    r = requests.get('https://sd7-api.herokuapp.com/api/authors/d3bb924f-f37b-4d14-8d8e-f38b09703bab/posts/9095cfd8-8f6a-44aa-b75b-7d2abfb5f694/', auth=('node01', 'P*ssw0rd!'))
    # print(r.text)
    
    post = r.json()
    # post = json.loads(r.json)

    # build the post ID and the author ID for the api call
    # post_id = 

    # get the post
    # post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'view-post.html', context)



class Post_Individual(GenericAPIView):
    serializer_class = PostSerializer
    # lookup_field = 'id'
    # lookup_url_kwarg = 'post_id'
    authentication_classes = []

    def get(self, request, author_id, post_id, format=None):
        """
        /authors/{author_id}/posts/{post_id}
        
        GET (local, remote): get the public post whose id is POST_ID
        """
        # print(f"looking for post with id={post_id}")
        # print(f"looking for post with authorid={author_id}")

        is_remote = RemoteAuth(request=request)
        if not is_remote:
            response = Response('Authentication credentials were not provided.', status=status.HTTP_401_UNAUTHORIZED)
            response['WWW-Authenticate'] = 'Basic realm="Enter your REMOTE credentials", charset="UTF-8"'
            return response

        # try:
        #     post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)
        # except Http404:
        #     if str(post_id).endswith('/'):
        #         post_id = post_id[:-1]
        #         post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)
        #     else:
        #         raise Http404
        post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, author_id, post_id, format=None):
        """
        /authors/{author_id}/posts/{post_id}
        
        POST (local): update the post whose id is POST_ID (must be authenticated)
        """
        # try:
        #     post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)
        # except Http404:
        #     if str(post_id).endswith('/'):
        #         post_id = post_id[:-1]
        #         post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)
        #     else:
        #         raise Http404
        post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)

        # do we have permission to edit this post?

        # are we authenticated?
        if not request.user.is_active:
            raise NotAuthenticated

        # are we admin or the author of this post
        auth = False
        if request.user.is_staff:
            auth = True
        elif str(request.user) == post.author_id:
            auth = True

        if not auth:
            raise PermissionDenied


        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['id'] != post.id:
                return Response("Changing post_id not allowed", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, author_id, post_id, format=None):
        """
        /authors/{author_id}/posts/{post_id}
        
        DELETE (local): remove the post whose id is POST_ID
        """
        post = get_object_or_404(Post.objects.all(), id=post_id, author_id=author_id)

        # do we have permission to edit this post?

        if not request.user.is_active:
            raise NotAuthenticated

        auth = False
        if request.user.is_staff:
            auth = True
        elif str(request.user) == post.author_id:
            auth = True

        if not auth:
            raise PermissionDenied
        
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def put(self, request, author_id, post_id, format=None):
        """
        /authors/{author_id}/posts/{post_id}
        
        PUT (local): create a post where its id is POST_ID
        """


        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        # do we have permission to create this post?

        if not request.user.is_active:
            raise NotAuthenticated

        auth = False
        if request.user.is_staff:
            auth = True
        elif str(request.user) == serializer.validated_data['author_id'] == author_id:
            auth = True

        if not auth:
            raise PermissionDenied
        
        # is the post id the same as our post_id
        if serializer.validated_data['id'] != post_id:
            return Response("Post's 'id' field doesn't match url post_id", status=status.HTTP_400_BAD_REQUEST)


        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



    def get_success_headers(self, data):
        try:
            return {'Location': str(data['id'])}
        except (TypeError, KeyError):
            return {}










# class ImagePost(APIView):
    
#     def get(self, request, author_id, post_id, format=None):
#         """
#         /authors/{author_id}/posts/{post_id}/image

#         GET (local, remote) get the public post converted to binary as an image
#         """
#         # return 404 if not an image
#         return Response({"message": f"Viewing image post with post_id {post_id} and author_id {author_id}"})





class All_Posts_By_Author(ListAPIView):
    serializer_class = PostSerializer
    # lookup_field = 'author_id'
    # lookup_url_kwarg = 'author_id'
    authentication_classes = []

    def get_queryset(self):
        return Post.objects.all()
    
    def get(self, request, author_id):
        
        is_remote = RemoteAuth(request=request)
        if not is_remote:
            response = Response('Authentication credentials were not provided.', status=status.HTTP_401_UNAUTHORIZED)
            response['WWW-Authenticate'] = 'Basic realm="Enter your REMOTE credentials", charset="UTF-8"'
            return response

        return super().get(request, author_id=author_id)


    def generate_unique_id(self, author_id):
        # time = quote(datetime.now(), safe='')
        time = str(uuid.uuid1())
        res = f"http://127.0.0.1:8000/authors/{author_id}/posts/{time}"
        return res

    # def post(self, request, author_id, format=None):
    #     """
    #     /authors/{author_id}/posts/

    #     POST (local) create a new post but generate a new id
    #     """

    #     request.data

    #     serializer = PostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # do we have permission to create this post?

    #     if not request.user.is_active:
    #         raise NotAuthenticated

    #     auth = False
    #     if request.user.is_staff:
    #         auth = True
    #     elif str(request.user) == serializer.validated_data['author_id'] == author_id:
    #         auth = True

    #     if not auth:
    #         raise PermissionDenied
        
    #     # is the post id the same as our post_id
    #     if serializer.validated_data['id'] != post_id:
    #         return Response("Post's 'id' field doesn't match url post_id", status=status.HTTP_400_BAD_REQUEST)


    #     serializer.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



    def get_success_headers(self, data):
        try:
            return {'Location': str(data['id'])}
        except (TypeError, KeyError):
            return {}




# These are extra, for testing purposes only. --------------------------------

class Post_All(APIView):

    def get(self, request, format=None):
        """
        GET all the post from the database. 
        """
        posts_query_set = Post.objects.all()
        serializer = PostSerializer(posts_query_set, many=True)
        return Response(serializer.data)



    def post(self, request, format=None):
        """
        POST a new post.
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

