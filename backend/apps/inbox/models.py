from django.db import models

from apps.authors.models import Author
from django.urls import reverse
# Create your models here.


class Inbox(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField(max_length=200, blank=True)
    source = models.CharField(max_length=50, blank=True)
    origin = models.CharField(max_length=50, blank=True)
    contentType = models.CharField(max_length=20, blank=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    
## should only have links to the post that includes author url

## id: uuid, 
# inbox ownerL uuid, 
# sender author : {url}, 
# summary: string, type: string (post, like, follow request, comment), 
# onc: 

# curl -u 'node01:P*ssw0rd!' https://sd7-api.herokuapp.com/api/authors/d3bb924f-f37b-4d14-8d8e-f38b09703bab/posts/9095cfd8-8f6a-44aa-b75b-7d2abfb5f694/
# inbox url, 
#     def commentlist_template():
#         return {"comments": "[]"}
    
#     def likeslist_template():
#         return {"likes":"[]"}
    
#     def followrequestlist_template():
#         return {"Follow Requests": "[]"}


#     comment_list = models.JSONField(blank=True, default=commentlist_template)
#     like_list = models.JSONField(blank=True, default=likeslist_template)
#     follow_request_list = models.JSONField(blank=True, default=followrequestlist_template)



# class Inbox(models.Model):
#     """
#     Here the author is the id of the author whos inbox is this
#     Post is the post sent to the person's inbox. Pretty straightforward. 
#     """
#     id = models.CharField(primary_key=True, max_length=255)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     dateTime = models.DateTimeField(auto_now_add=True)
