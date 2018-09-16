from django.db import models


class MediaObject(models.Model):
    title = models.CharField(max_length=200, default=None, null=True)
    artist = models.CharField(max_length=100, default=None, null=True)
    user = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200, default=None, null=True)
    time_posted = models.DateTimeField('posted at', auto_now_add=True)
    service = models.CharField(max_length=15)

    def __str__(self):
        return self.url
