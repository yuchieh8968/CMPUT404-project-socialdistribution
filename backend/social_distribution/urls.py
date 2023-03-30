"""social_distribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, register_converter
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from apps.authors.views import Author_All, Author_Individual, SignUp
from apps.posts.views import Post_Individual, All_Posts_By_Author, GuiPost
from django.views.generic.base import RedirectView
from apps.inbox.views import InboxListCreateView
from apps.likes.views import Post_A_Like, Get_Like_For_Post

# class AuthorIDConverter:
#       regex = r".+?(?=\/posts)"

#       def to_python(self, value: str) -> str:
#           return value

#       def to_url(self, value: str) -> str:
#           return value

# register_converter(AuthorIDConverter, "author_id_path")


urlpatterns = [

    # sign-up
    path('signup', SignUp.as_view(), name="sign-up"),

    # posts
    path('api/authors/<str:author_id>/posts/<str:post_id>', Post_Individual.as_view(),
         name="Specific post"),                                     # Specific post
    # Recent posts from author, or create new one with new id
    path('api/authors/<str:author_id>/posts/',
         All_Posts_By_Author.as_view(), name="Recent posts by author"),

    # authors
    path('api/authors/<str:author_id>/', Author_Individual.as_view(),
         name="Single author"),                                # Single author
    # All authors
    path('api/authors/', Author_All.as_view(), name="All authors"),

    # redirect home to api/docs/
    # https://stackoverflow.com/questions/14959217/django-url-redirect
    path('', RedirectView.as_view(url='api/docs/', permanent=False), name='index'),

    # admin, auth, api-schema, and api docs
    # Django admin site
    path('admin/', admin.site.urls),
    # Prefix for API login and logout
    path('api/auth/', include('rest_framework.urls')),
    # API schema endpoint (used for dynamic swagger docs generation)
    path('api/schema/', get_schema_view(), name='API Schema'),
    path('api/docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'API Schema'}
    ), name='swagger-ui'),                                          # Prefix for documentation pages (currently /docs/api/ only)

    # path('authors/<str:author_text>/posts/<str:post_text>', GuiPost, name="Gui Post"),
    path('remote-post', GuiPost, name="Gui Post"),

    # # followers
    # path('api/authors/<path:author_id>/followers', XXX, name="Author_id's followers"),                                       # Author_id's followers
    # path('api/authors/<path:author_id>/followers/<path:foreign_author_id>', XXX, name="Follower of author_id"),               # Specific follower of author_id

    # # posts
    # path('api/authors/<path:author_id>/posts/<path:post_id>/image', XXX, name="Image post"),                                  # Image post

    # # comments
    # path('api/authors/<path:author_id>/posts/<path:post_id>/comments', XXX, name="Comments on post"),                         # Comments on post

    # # likes
    # Send like to author
    path('api/authors/<str:author_id>/inbox/',
         Post_A_Like.as_view(), name="Send like to author"),
    path('api/authors/<str:author_id>/posts/<str:post_id>/likes', Get_Like_For_Post.as_view(),
         name="Likes on post"),                               # Get likes on post
    # path('api/authors/<path:author_id>/posts/<path:post_id>/comments/<path:comment_id>/likes', XXX, name="Likes on comment"),  # Get likes on comment
    # path('api/authors/<path:author_id>/liked', XXX, name="Author likes"),                                                    # See what author_id has liked

    # # inbox
    # Inbox = new posts from who you follow
    path('api/authors/<path:author_id>/inbox',
         InboxListCreateView.as_view(), name="Inbox"),
]
