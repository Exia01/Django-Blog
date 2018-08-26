from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # add in thumbnail later
    # add  in author later
    # def __str__(self):
    #     return self.title
    def __str__(self):
        return "<Article {} | {} {} >".format(self.title, self.slug, self.date)

    # this is techically a model method. 
    def snippet(self):
        return self.body[:50] + '...'
