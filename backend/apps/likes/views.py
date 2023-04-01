from django.shortcuts import render

# Create your views here.


class Post_A_Like(GenericAPIView):
    serializer_class = LikeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, author_id, format=None):
        """
        URL: ://service/authors/{AUTHOR_ID}/inbox/
        POST [local, remote]: send a like object to AUTHOR_ID
        """

        serializer = LikeSerializer(Like, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Get_Like_For_Post(GenericAPIView):
    serializer_class = LikeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, author_id, post_id):
        # Filtering the query to get likes
        try:
            query_obj = Like.objects.filter(author__id=author_id)
            query_obj2 = query_obj.filter(
                object__icontains=str(f'{post_id}'))
            return query_obj2
        except:
            raise Http404

    def get(self, request, author_id, post_id, format=None):
        """
        URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/likes
        GET [local, remote] a list of likes from other authors on AUTHOR_ID’s post POST_ID
        """
        obj = self.get_object(author_id, post_id)
        serializer = LikeSerializer(obj, many=True)
        return Response(serializer.data)
