from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView
from .models import Inbox
from .serializer import InboxSerializer
from apps.authors.models import Author
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        authorID= self.kwargs.get("author_id","")
        return self.queryset.filter(author_id = authorID).order_by("-created_at")
    
    def perform_create(self, serializer):
        authorID= self.kwargs.get("author_id","")
        authorInstance = Author.objects.get(id = authorID) #SQL select * from author where ID = author
        return serializer.save(author_id = authorInstance)
    