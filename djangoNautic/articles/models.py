from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True) # if image is not given, then it will automatically select one for us. 
    author = models.ForeignKey(User, default=None)
    # def __str__(self):
    #     return self.title
    def __str__(self):
        return "<Article {} | {} {} >".format(self.title, self.slug, self.date)

    # this is techically a model method. 
    def snippet(self):
        return self.body[:50] + '...'
