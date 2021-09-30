from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import Group
from rest_framework.response import *
from rest_framework.views import *
from rest_framework.permissions import IsAuthenticated 
from .serializer import *



class SnippetApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, req, pk=None):
        if pk is not None:
            _snippet = Snippet.objects.filter(id = pk)
            _serializer = SnippeteSerializer(_snippet[0])
            return Response(_serializer.data)
        
        _snippet = Snippet.objects.all()
        _count = Snippet.objects.all().count()
        _serializer = SnippeteSerializer(_snippet, many=True)
        context = {
            'count' : _count,
            'snippets' : _serializer.data
        }
        return Response(context)
    
    def post(self, req):
        _tag = req.data.get('tag')
        _user = User.objects.get(username = req.user.username)
        _tag_data = Tag.objects.get_or_create(name=_tag)

        context = {
            'user' : _user.pk,
            'title' : req.data.get('title'),
            'text' : req.data.get('text'),
            'tag' : _tag_data[0].name
        }
        _serializer = AllSnippeteSerializer(data = context)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data)
        else:
            return Response(_serializer.errors)

    def put(self, req, pk):
        _snippet = Snippet.objects.get(id=pk)
        _serializer = SnippeteSerializer(_snippet, data = req.data, partial=True)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, req, pk):
        _snippet = Snippet.objects.get(id=pk)
        _snippet.delete()
        _serializer = SnippeteSerializer(_snippet)
        return Response(_serializer.data)
            

class TagApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, req):
        _tag = Tag.objects.all()
        _serializer = TagSerializer(_tag, many=True)
        return Response(_serializer.data)
    
    def post(self, req):
        _tag = req.data.get('tag')
        _snippet = Snippet.objects.filter(tag__name = _tag)
        _serializer = SnippeteSerializer(_snippet, many = True)
        return Response(_serializer.data)
    