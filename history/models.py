from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_text = models.CharField(max_length=20)
    artist_details = models.CharField(max_length=200)
    def __str__(self):
        return self.artist_text


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_text = models.CharField(max_length=50)
    def __str__(self):
        return self.song_text