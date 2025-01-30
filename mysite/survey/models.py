
# Create your models here.

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='survey')
    slug = models.SlugField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('survey:list_survey', args=[self.slug])



class PostQuestion(models.Model):
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='questions')

    def __str__(self):
        return self.text



class PostAnswer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(PostQuestion, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text

class Comment(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
