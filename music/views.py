from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<H1>This is the Music App Homepage</h1>')

def detail(response, album_id):
    return HttpResponse('<H2>Details for AlbumID: ' + str(album_id) + '</H2>')
