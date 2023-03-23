from rest_framework.response import Response
from rest_framework.request import Request
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.exceptions import NotAuthenticated, PermissionDenied


# Create your views here.

class Author_All(ListAPIView):
    """
    /authors/

    GET (local, remote): Used to view all authors
    """
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()


class Author_Individual(GenericAPIView):
    serializer_class = AuthorSerializer
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
            if serializer.validated_data['id'] != author.id:
                return Response("Changing author_id not allowed", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
