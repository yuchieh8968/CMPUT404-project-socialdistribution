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
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from apps.authors.views import Author_All, Author_Individual
from django.views.generic.base import RedirectView


urlpatterns = [

    # redirect home to api/docs/
    # https://stackoverflow.com/questions/14959217/django-url-redirect
    path('', RedirectView.as_view(url='api/docs/', permanent=False), name='index'),

    # admin, auth, api-schema, and api docs
    path('admin/', admin.site.urls),                                # Django admin site
    path('api/auth/', include('rest_framework.urls')),              # Prefix for API login and logout
    path('api/schema/', get_schema_view(), name='API Schema'),      # API schema endpoint (used for dynamic swagger docs generation)
    path('api/docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'API Schema'}
    ), name='swagger-ui'),                                          # Prefix for documentation pages (currently /docs/api/ only)


    # authors
    path('api/authors/', Author_All.as_view(), name="All authors"),                                                         # All authors
    path('api/authors/<str:author_id>/', Author_Individual.as_view(), name="Single author"),                                # Single author

    # # followers
    # path('api/authors/<str:author_id>/followers', XXX, name="Author_id's followers"),                                       # Author_id's followers
    # path('api/authors/<str:author_id>/followers/<str:foreign_author_id>', XXX, name="Follower of author_id"),               # Specific follower of author_id

    # # posts
    # path('api/authors/<str:author_id>/posts/', XXX, name="Recent posts by author"),                                         # Recent posts from author, or create new one with new id
    # path('api/authors/<str:author_id>/posts/<str:post_id>', XXX, name="Specific post"),                                     # Specific post
    # path('api/authors/<str:author_id>/posts/<str:post_id>/image', XXX, name="Image post"),                                  # Image post

    # # comments
    # path('api/authors/<str:author_id>/posts/<str:post_id>/comments', XXX, name="Comments on post"),                         # Comments on post

    # # likes
    # path('api/authors/<str:author_id>/inbox/', XXX, name="Send like to author"),                                            # Send like to author
    # path('api/authors/<str:author_id>/posts/<str:post_id>/likes', XXX, name="Likes on post"),                               # Get likes on post
    # path('api/authors/<str:author_id>/posts/<str:post_id>/comments/<str:comment_id>/likes', XXX, name="Likes on comment"),  # Get likes on comment
    # path('api/authors/<str:author_id>/liked', XXX, name="Author likes"),                                                    # See what author_id has liked

    # # inbox
    # path('api/authors/<str:author_id>/inbox', XXX, name="Inbox"),                                                           # Inbox = new posts from who you follow
]
