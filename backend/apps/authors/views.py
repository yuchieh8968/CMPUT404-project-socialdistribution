from rest_framework.response import Response
from rest_framework.request import Request
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.views import generic
from .admin import CustomUserCreationForm
# from apps.authors.remoteauth import RemoteAuth


# Create your views here.


#https://learndjango.com/tutorials/django-signup-tutorial
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = "api/auth/login/"
    template_name = "signup.html"



class Author_All(ListAPIView):
    """
    /authors/

    GET (local, remote): Used to view all authors
    """
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Author.objects.all()
    
    def get(self, request, *args, **kwargs):
        # is_remote = RemoteAuth(request=request)
        # if not is_remote:
        #     response = Response('Authentication credentials were not provided.', status=status.HTTP_401_UNAUTHORIZED)
        #     response['WWW-Authenticate'] = 'Basic realm="Enter your REMOTE credentials", charset="UTF-8"'
        #     return response
        return super().get(request)


class Author_Individual(GenericAPIView):
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'author_id'

    def get_queryset(self):
        return Author.objects.all()


    def get(self, request, author_id, format=None):
        """
        /authors/{author_id}/
        
        GET (local, remote): retrieve AUTHOR_ID profile
        """
        author = get_object_or_404(queryset=self.get_queryset(), id=author_id)
        serializer = self.serializer_class(author)
        return Response(serializer.data)

    def post(self, request: Request, author_id, format=None):
        """
        /authors/{author_id}/
        
        POST (local): update AUTHOR_ID profile
        """
        author = get_object_or_404(queryset=self.get_queryset(), id=author_id)


        # do we have permission to edit this author?

        if not request.user.is_active:
            raise NotAuthenticated

        auth = False
        if request.user.is_staff:
            auth = True
        elif str(request.user) == author_id:
            auth = True

        if not auth:
            raise PermissionDenied


        serializer = self.serializer_class(author, data=request.data)

        if serializer.is_valid():
            if 'id' in serializer.validated_data.keys():
                if serializer.validated_data['id'] != author.id:
                    return Response("Changing author_id not allowed", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
