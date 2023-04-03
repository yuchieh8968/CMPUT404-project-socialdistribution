from rest_framework.response import Response
from rest_framework.request import Request
from .models import Author
from .serializers import AuthorSerializer, InfoSerializer, AnyProfileSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.views import generic
from .admin import CustomUserCreationForm, CustomUserChangeForm
# from apps.authors.remoteauth import RemoteAuth
from django.shortcuts import render
import requests
from requests import Response as res
from urllib.parse import urlparse
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from apps.posts.models import Post
from apps.followers.models import Follow


# Create your views here.

def Test(request):
    author = request.user
    if not author.is_active:
        return redirect(reverse_lazy('login'))
    # numposts = len(Post.objects.filter(author=author))
    # numfollowers =  len(Follow.objects.filter(object=author))
    # # numfollowing = len(Follow.objects.filter(actor=author.build_author_id()))
    context = {}
    return render(request, 'test.html', context)



#https://learndjango.com/tutorials/django-signup-tutorial
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = "/login/"
    template_name = "signup.html"

class EditProfile(generic.UpdateView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
    pagination_class = None

    # form_class = CustomUserChangeForm

    success_url = "/profile/"
    template_name = "edit-profile.html"
    model = Author

    fields = ['displayName', 'github', 'profileImage']

    def get_object(self):
        author = self.request.user
        if not author.is_active:
            return redirect(reverse_lazy('login'))
        return author

    # def dispatch(self, request, *args, **kwargs):
    #     author = request.user
    #     if not author.is_active:
    #         return redirect(reverse_lazy('login'))
    #     self.object = author
    #     return super().dispatch(request, *args, **kwargs)

    


class MyInfo(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InfoSerializer
    pagination_class = None
    
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
    

def LocalProfileEdit(request):
    author = request.user
    if not author.is_active:
        return redirect(reverse_lazy('login'))
    numposts = len(Post.objects.filter(author=author))
    numfollowers =  len(Follow.objects.filter(object=author))
    # numfollowing = len(Follow.objects.filter(actor=author.build_author_id()))
    return render(request, 'profile-edit.html', {"author": author, "numposts": numposts, "numfollowers" : numfollowers})#, "numfollowing": numfollowing })

from rest_framework.parsers import FormParser
from rest_framework.decorators import parser_classes
class AnyProfileView(GenericAPIView):
    """
    Used to render an author's profile, except the profile can be from any of our connected teams.
    POST request body just requires the url to fetch the author's profile.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AnyProfileSerializer
    pagination_class = None
    parser_classes = [FormParser]

    def post(self, request: Request):

        serializer = AnyProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = serializer.validated_data["url"]
        if not url.endswith('/'):
            url = url + '/'

        host = urlparse(url).hostname

        if host in settings.CONNECTED_TEAMS:
            user = settings.CONNECTED_TEAMS[host]["username"]
            password = settings.CONNECTED_TEAMS[host]["password"]
            r : res = requests.get(url, auth=(user, password))
            context = r.json()

            # can we get numposts and numfollowers here?

            print(context["url"])
            r_posts : res = requests.get(context["url"] + '/posts/', auth=(user, password))
            if r_posts.status_code == 200 and 'count' in r_posts.json().keys():
                context["numposts"] = r_posts.json()['count']
            else:
                context["numposts"] = "?"


            r_followers : res = requests.get(context["url"] + '/followers/', auth=(user, password))
            if r_followers.status_code == 200 and 'count' in r_followers.json().keys():
                context["numfollowers"] = r_followers.json()['count']
            else:
                context["numfollowers"] = "?"

            return render(request, 'profile-view.html', context)
        else:
            raise Http404


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
