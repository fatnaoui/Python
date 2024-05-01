from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Article(models.Model):
    slug=models.SlugField(null=False,blank=False)  # not null in the database and not empty in frontend
    title=models.CharField(max_length=256)
    description=models.TextField()
    body=models.TextField()
    tags=models.ManyToManyField('Tag',blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    favorited=models.BooleanField()
    favoritesCount=models.IntegerField(default=0)
    def __str__(self):
        return self.title