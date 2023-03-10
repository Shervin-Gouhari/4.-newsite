from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    class Meta:
        ordering = ("-publish",)
        
    STATUS = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="draft")
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse("blogs:detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
    
    
    