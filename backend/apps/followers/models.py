# from django.db import models

# from apps.authors.models import Author
# # Create your models here.



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

