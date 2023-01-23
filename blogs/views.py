from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

def post_list_view(request):
    posts = Post.published.all().order_by("publish")
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, "blogs/list.html", {"post_list": post_list})

# class PostListView(ListView):
#     queryset = Post.published.all().order_by("publish")
#     paginate_by = 2     # sends "page_obj"
#     template_name = "blogs/list.html"
    
    
def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, status="published", publish__year=year, publish__month=month, publish__day=day, slug=post)
    return render(request, "blogs/detail.html", {"post": post})


