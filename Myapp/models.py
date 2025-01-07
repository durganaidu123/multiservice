from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

