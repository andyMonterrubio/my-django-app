from django.shortcuts import render
from weblog.models import Post, Comment, Category

# Create your views here.
#request: Django provides the object 
def blog_index(request):
    #return last 10 elements
    posts = Post.objects.filter(is_published=True).order_by("-date")

    return render(
        request, 
        "index.html", 
        context = { "posts": posts }
    )

