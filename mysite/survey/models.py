from django.db import models

# Create your models here.

from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone
from django.urls import reverse



# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
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


