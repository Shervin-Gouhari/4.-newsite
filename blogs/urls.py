from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.post_list_view, name="list"),
    # path("", views.PostListView.as_view(), name="list"),
    path("detail/<int:year>/<int:month>/<int:day>/<slug:post>", views.post_detail_view, name="detail"),
]
