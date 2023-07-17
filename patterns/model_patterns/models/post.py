from django.db import models

from patterns.model_patterns.manager import PostManager

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    POST_TYPES = (
        (0, 'public'),
        (1, 'private'),
    )
    text = models.TextField()
    privacy= models.IntegerField(max_length=1, null=True, choices=POST_TYPES)
    objects = PostManager()
