from django.db import models
from django.conf import settings
from django.utils.timezone import now

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
        (Programming, 'Programming'),(Random, 'Random'))





    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    Category = models.CharField(max_length=200, choices=YEAR_IN_SCHOOL_CHOICES, null=True)
    # topic = models.CharField(max_length=200, choices=YEAR_IN_SCHOOL_CHOICES, null=True)      ## Might have options for Foreign key concept for further detailed (level-3 type) filtered posts
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.title


## we will need a publish method.



class Comment(models.Model):
    post = models.ForeignKey('BlogSite.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)
    
    def __str__(self):
        return self.text

