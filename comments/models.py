from django.db import models
from customusers.models import CustomUser
from videos.models import Video

# Create your models here.

class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_recipe = models.ForeignKey(Video, related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.parent_recipe.title, self.author)