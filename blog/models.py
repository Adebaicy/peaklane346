from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=30)
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering=('-created_on',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail',args=[self.slug])