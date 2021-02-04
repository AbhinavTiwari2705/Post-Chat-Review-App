from django.db import models
from django.conf import settings
from django.utils.timezone import now
import uuid
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    TheClimateCrisis = 'The Climate Crisis'
    Food = 'Food'
    MoviesWebseries = 'Movies/Webseries'
    Random = 'Random'
    Programming = 'Programming'
    YEAR_IN_SCHOOL_CHOICES = (
        (TheClimateCrisis, 'The Climate Crisis'),
        (Food, 'Food'),
        (MoviesWebseries, 'Movies/Webseries'),
        (Programming, 'Programming'),
        (Random, 'Random'))


    temp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=200)
    Category = models.CharField(max_length=200, choices=YEAR_IN_SCHOOL_CHOICES, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    published_date = models.DateTimeField(blank=True, null=True, default=now)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.temp_id)])





class Comment(models.Model):
    post = models.ForeignKey('BlogSite.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)


    def __str__(self):
        return self.text

