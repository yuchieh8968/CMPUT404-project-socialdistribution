from django.db import models
import uuid
from apps.authors.models import Author
# Create your models here.


"""

{
    "type": "Follow",      
    "summary":"Greg wants to follow Lara",
    "actor":{
        "type":"author",
        "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        "host":"http://127.0.0.1:5454/",
        "displayName":"Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "object":{
        "type":"author",
        # ID of the Author
        "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        # the home host of the author
        "host":"http://127.0.0.1:5454/",
        # the display name of the author
        "displayName":"Lara Croft",
        # url to the authors profile
        "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        # HATEOS url for Github API
        "github": "http://github.com/laracroft",
        # Image from a public domain
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    }
}


"""
class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    actor = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)
    object = models.URLField(null=False, blank=False)

# class Follow(models.Model):
#     pass



# # https://stackoverflow.com/questions/58794639/how-to-make-follower-following-system-with-django-model
# class Author_Follows(models.Model):
#     """
#     Each individual record is a someone following someone. So, all the following/Friend
#     info is here.
#     author_id is the id of the author who is following.
#     following_author_id is the id of the author who is being followed.
#     """
#     author_id = models.ForeignKey(Author, related_name="following", on_delete=models.CASCADE)

#     following_author_id = models.ForeignKey(Author, related_name="followers", on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)# db_index=True)

#     pending = models.BooleanField("Pending", default=True)


#     # follow request using
#     # Author_Follows.objects.create(author_id=author.id,following_author_id=follow.id)


#     # fetch using
#     # author = Author.objects.get(id = ?)
#     # author.following.all()
#     # author.followers.all()

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['author_id','following_user_id'],  name="unique_followers")
#         ]
#         ordering = ["-created"]


#     def __str__(self):
#         return f"{self.author_id} is following {self.following_author_id}"

