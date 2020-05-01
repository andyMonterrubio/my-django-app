from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        #to change the word
        verbose_name_plural = "Categories" 

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    #type of var
    title = models.CharField(max_length=500) 
    body = models.TextField()
    date = models.DateTimeField()
    is_published = models.BooleanField() 
    #add reference to category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) 

    #method to show title in admin page 
    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.username