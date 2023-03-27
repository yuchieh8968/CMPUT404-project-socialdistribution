from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView
from .models import Inbox
from .serializer import InboxSerializer

# Create your views here.
# def inbox(request: Request, author_id: str, post_url: str):
#     """
#     /authors/{author_id}/inbox

#     GET (local, remote): retrieve posts in inbox

#     """

#     return Response({"message": "Viewing all Inbox Notifications"})
class InboxListCreateView(ListCreateAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer
    def get_queryset(self):
        authorID= self.kwargs.get("author_id","")
        return self.queryset.filter(author_id = authorID).order_by("-created_at")