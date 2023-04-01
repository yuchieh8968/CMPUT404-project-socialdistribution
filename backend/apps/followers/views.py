from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView
from .models import Follow
from apps.authors.models import Author
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from apps.followers.serializers import FollowSerializer
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
class FollowerListCreateView(ListCreateAPIView):
    queryset = Follow.objects.all()

    authentication_classes = [BasicAuthentication]
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        authorID= self.kwargs.get("author_id","")
        return self.queryset
    
    def perform_create(self, serializer):
        authorID= self.kwargs.get("author_id","")
        authorInstance = Author.objects.get(id = authorID) #SQL select * from author where ID = author
        return serializer.save()


# gets current url. Will use this later to parse out author (current logged in user) url
def my_view(request):
    current_url = request.build_absolute_uri()
    return HttpResponse(current_url)



class Follower(APIView):

    def get(self, request, author_id, foreign_author_id, format=None):
        """
        /authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

        GET (local, remote): check if FOREIGN_AUTHOR_ID is a follower of AUTHOR_ID
        """
        return Response({"message": f"Checking if author {foreign_author_id} follows author {author_id}"})
    
    def put(self, request, author_id, foreign_author_id, format=None):
        """
        /authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

        PUT (local): Add FOREIGN_AUTHOR_ID as a follower of AUTHOR_ID (must be authenticated)
        """
        return Response({"message": f"Adding author {foreign_author_id} as a follower of author {author_id}"})

    def delete(self, request, author_id, foreign_author_id, format=None):
        """
        /authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

        DELETE (local): remove FOREIGN_AUTHOR_ID as a follower of AUTHOR_ID
        """
        return Response({"message": f"Removing author {foreign_author_id} as a follower of author {author_id}"})
    

