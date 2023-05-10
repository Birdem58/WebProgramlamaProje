from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user.models import Profile

# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               blank=False
                               )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT)
    likes = models.ManyToManyField(User, blank=True, related_name="blog_posts")

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def str(self):
        return self.title
