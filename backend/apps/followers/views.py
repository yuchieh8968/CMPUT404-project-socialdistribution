from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import Follow
from apps.authors.models import Author
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from apps.followers.serializers import FollowSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status



# Create your views here.
class FollowerCreateView(GenericAPIView):
    queryset = Follow.objects.all()
    authentication_classes = [BasicAuthentication]
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    

    def put(self, request, *args, **kwargs):
        author_instance = Author.objects.get(id=kwargs.get("author_id"))
        new_follower_data = {"actor":kwargs.get("foreign_author_id"),"object":kwargs.get("author_id")}
        serializer = self.get_serializer(data=new_follower_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        try:
            instance = Follow.objects.get(actor=kwargs.get("foreign_author_id"), object=kwargs.get("author_id"))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        try:
            instance = Follow.objects.get(actor=kwargs.get("foreign_author_id"), object=kwargs.get("author_id"))
            instance.delete()
        except Follow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# gets current url. Will use this later to parse out author (current logged in user) url
def my_view(request):
    current_url = request.build_absolute_uri()
    return HttpResponse(current_url)

class FollowerListCreateView(ListAPIView):
    queryset = Follow.objects.all()
    authentication_classes = [BasicAuthentication]
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    #  ----------- override the GET
    def get(self, request, author_id):
        return super().get(request, author_id=author_id)