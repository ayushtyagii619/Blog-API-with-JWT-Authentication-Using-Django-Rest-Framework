from django.urls import path,include
from .views import LikeApiView, CategoryView , PostView,CommentView
from rest_framework.routers import DefaultRouter

app_name = "blog_post"
router = DefaultRouter()
router.register(r"categories",CategoryView)
router.register(r"^(?P<post_id>\d+)/comment",CommentView)
router.register(r"",PostView)

urlpatterns = [
    path("",include(router.urls)),
    path(("like/<int:pk>/"),LikeApiView.as_view(),name='post-like'),
]
