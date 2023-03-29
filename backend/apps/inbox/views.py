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
from django.http import HttpResponse, JsonResponse
 

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

# send post object into frontend
def get_post_data(request):
    # data = {
    #     "author": "http://127.0.0.1:8000/api/authors/7427ff62-5d48-4bb9-91b3-3816a4487afe",
    #     "object": "http://127.0.0.1:8000/api/authors/7427ff62-5d48-4bb9-91b3-3816a4487afe/posts/de3bc74a-a1a3-4a49-ba5b-d63875d6a027",
    #     "type": "Post",
    #     "summary": "Sent Post"
    # }
    data = {"message": "Hello from the backend!"}

    return JsonResponse(data)

def my_view(request):
    current_url = request.build_absolute_uri()
    return HttpResponse(current_url)