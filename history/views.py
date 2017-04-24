from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



from django.http import HttpResponse
from django.views import generic

from .models import Artist, Song


class IndexView(generic.ListView):
    model = Artist
    template_name = 'history/index.html'
    context_object_name = 'artist_list'

class SongsView(generic.DetailView):
    model = Artist
    template_name = 'history/songs.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Artist.objects