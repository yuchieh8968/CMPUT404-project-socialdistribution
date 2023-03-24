from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
@api_view(['GET'])
def inbox(request: Request, author_id: str, post_url: str):
    """
    /authors/{author_id}/inbox

    GET (local, remote): retrieve posts in inbox

    """

    return Response({"message": "Viewing all Inbox Notifications"})
