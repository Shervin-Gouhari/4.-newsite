# for further information on queries, search django queries on Google
from django.contrib.auth.models import User
from blogs.models import Post

user = User.objects.get(username="admin")

post = Post(title="third post", slug="third_post", body="this is third post body", author=user)
post.save()
# or
Post.objects.create(title="forth post", slug="forth_post", body="this is forth post body", author=user)

post.title = "third"
post.save()

all_posts = Post.objects.all()

Post.objects.filter(publish__year=2023)
Post.objects.filter(publish__year=2023, author__username="admin")
Post.objects.filter(publish__year=2023, author__username="admin").exclude(title__startswith="new")

Post.objects.order_by("title")
Post.objects.order_by("publish")
Post.objects.order_by("-publish")

post = Post.objects.get(id=1)
post.delete()

# -----

from blogs.models import Post

published_posts = Post.published.all()
published_posts

posts = Post.objects.all()
posts