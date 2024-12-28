from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, CommentViewSet

app_name = "social_media_action"

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
