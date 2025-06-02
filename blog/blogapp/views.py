from django.shortcuts import render, get_object_or_404
from blogapp.models import Post

# Create your views here.
def all_post(request):
    post = Post.objects
    return render(request, 'posts.html', {'post':post})

def detail(request, blog_id):
    detail = get_object_or_404(Post, pk = blog_id)
    return render(request, 'details.html', {'post':detail})