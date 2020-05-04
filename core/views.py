from django.http import JsonResponse
from django.shortcuts import render

# third party imports 
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .serializer import PostSerializer
from .models import Post


class TestView(APIView):
    def get(self, request ,*args, **kwargs):
        qs = Post.objects.all()
        serilaizer = PostSerializer(qs,many=True)
        return Response(serilaizer.data)


    def post(self, request ,*args, **kwargs):
        serilaizer = PostSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        
        return Response(serilaizer.errors)
      
