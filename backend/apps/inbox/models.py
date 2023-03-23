from django.db import models
from django.urls import reverse
# Create your models here.


# class Inbox(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     url = models.URLField(max_length=200, blank=True)
    

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
