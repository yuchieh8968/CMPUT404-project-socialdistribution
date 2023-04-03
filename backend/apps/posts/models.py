from django.db import models
from django.urls import reverse

from apps.authors.models import Author
from django.contrib.postgres.fields import ArrayField
from urllib.parse import quote
import uuid
from django.conf import settings
from apps.followers.models import Follow
from urllib.parse import urlparse
import requests
# Create your models here.


class Post(models.Model):

    # Fields
    id = models.CharField(max_length=256, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, blank=False, null=False)
    source = models.CharField(max_length=256, blank=True, null=True)
    origin = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    CONTENT_CHOICES = (
        ("text/plain", "text/plain"),
        ("text/markdown", "text/markdown"),
        ("application/base64", "application/base64"),
        ("image/png;base64", "image/png;base64"),
        ("image/jpeg;base64", "image/jpeg;base64")
    )
    contentType = models.CharField(
        choices=CONTENT_CHOICES, max_length=20, default="text/plain")
    
    content = models.TextField(blank=False, null=False) # changed to textfield for images
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    categories = ArrayField(models.CharField(max_length=20, blank=True), blank=True)

    # count = models.PositiveBigIntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True)
    VISIBIILTY_CHOICES = (
        ("PUBLIC", "PUBLIC"),
        ("PRIVATE", "PRIVATE"),
    )
    visibility = models.CharField(max_length=10, choices=VISIBIILTY_CHOICES, default="PUBLIC")
    
    unlisted = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title
    
    def build_id(self):
       host = settings.HOST
       return f"{host}/api/authors/{str(self.author)}/posts/{str(self.id)}"
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            # self.id = quote(self.id, safe='')
            OnPostCreate_SendToInboxes(self.author, self)
            super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['published']




def OnPostCreate_SendToInboxes(author: Author, post: Post):
    """
    When a PUBLIC post is created, send it to the inboxes of everyone who follows me
    When a PRIVATE post is created, send it to the inboxes of my true friends (I follow them and they follow me)
    """
    print("POST CREATED! SENDING TO INBOXES")
    author_urls_to_send_to = []
    people_who_follow_me = []
    people_who_follow_me = Follow.objects.filter(object = author)
    print(f"Author {author.displayName} has {len(people_who_follow_me)} followers")
    my_url = author.build_author_id()

    if post.visibility == "PUBLIC" and post.unlisted == False:
        for follower in people_who_follow_me:
            author_urls_to_send_to.append(follower.actor)
    # elif post.visibility == "PRIVATE":
    #     people_i_follow = Follow.objects.filter(actor= author.build_author_id())
    #     # get followers that follow me back
    #     for follower in people_who_follow_me:
    #         # check if we are following them
    #         # requires API call?
    #         for person_i_follow in people_i_follow:
    #             if 


    for url in author_urls_to_send_to:
        # send to this authors inbox, for now lets do local
        if not url.endswith('/'):
            url += '/'
        url += 'inbox/'
        print(f"sending post to {url}")
        host = urlparse(url).hostname
        if host in settings.CONNECTED_TEAMS:
            user = settings.CONNECTED_TEAMS[host]["username"]
            password = settings.CONNECTED_TEAMS[host]["password"]

            d = {"author": my_url,
                 "object": post.build_id(),
                 "type": "post",
                 "summary": f"{author.displayName} created a post"}

            r = requests.post(url, auth=(user, password), data=d)
            result = r.json()
            print(result)
    print("DONE")