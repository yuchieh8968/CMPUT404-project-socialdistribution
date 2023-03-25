from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Author_Followers(APIView):

    def get(self, request, author_id, format=None):
        """
        /authors/{AUTHOR_ID}/followers 

        GET (local, remote): get a list of authors who are AUTHOR_Ids followers
        """
        return Response({"message": f"Viewing the followers of author {author_id}"})
    
    
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