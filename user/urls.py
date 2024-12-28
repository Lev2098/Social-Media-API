from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import (
    CreateUserView,
    ManageUserView,
    LogoutView,
    CustomTokenObtainPairView,
    UserProfileViewSet,
    FollowUnfollowView,
    FollowersListView,
    FollowingListView,
)

app_name = "user"
router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet, basename="user-profile")
urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("account/", ManageUserView.as_view(), name="manage"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/<int:user_id>/follow/", FollowUnfollowView.as_view(), name="follow"),
    path(
        "users/<int:user_id>/unfollow/", FollowUnfollowView.as_view(), name="unfollow"
    ),
    path(
        "users/<int:user_id>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    path(
        "users/<int:user_id>/following/",
        FollowingListView.as_view(),
        name="following-list",
    ),
    path("", include(router.urls)),
]
