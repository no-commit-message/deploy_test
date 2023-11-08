from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


class PostviewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def testview(request):
    return render(request, 'index.html')