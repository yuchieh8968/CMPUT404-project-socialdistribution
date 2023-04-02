from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
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
        print("XXXX")
        author_instance = Author.objects.get(id=kwargs.get("author_id"))
        new_follower_data = {"actor":kwargs.get("foreign_author_id"),"object":kwargs.get("author_id")}
        print(new_follower_data)
        serializer = self.get_serializer(data=new_follower_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

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
    

