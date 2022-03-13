from django.db import models


class StreamPlatForm(models.Model):
    name = models.CharField(max_length=120)
    about = models.CharField(max_length=120)
    website = models.URLField(max_length=120)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=120)
    storyline = models.CharField(max_length=120)
    platform = models.ForeignKey(StreamPlatForm, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=120)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="review")
    active = models.BooleanField()
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)



