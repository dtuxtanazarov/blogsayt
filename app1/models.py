from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text = models.TextField()
    author =models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detailpost', args=[str(self.pk)])