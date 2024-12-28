from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from social_media_action.permission import IsOwnerOrReadOnly
from user.models import User
from user.serializers import UserSerializer, UserProfileSerializer, FollowSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Login
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Logout
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logout successful."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def retrieve(self, request, *args, **kwargs):
        """
        Users can view profiles by ID.
        """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Check if the "me" query parameter is present
        """
        if "me" in request.query_params:
            self.queryset = self.queryset.filter(id=request.user.id)
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Allow users to delete only their own profile.
        """
        instance = self.get_object()
        if instance != request.user:
            raise PermissionDenied("You do not have permission to delete this profile.")
        self.perform_destroy(instance)
        return Response(
            {"detail": "Your profile has been deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )


class FollowUnfollowView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id):
        """following a user"""
        try:
            target_user = User.objects.get(id=user_id)
            if request.user == target_user:
                return Response(
                    {"detail": "You cannot follow yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if target_user.followers.filter(id=request.user.id).exists():
                return Response(
                    {"detail": "You are already following this user."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            target_user.followers.add(request.user)
            return Response(
                {"detail": f"You are now following {target_user.username}."},
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, user_id):
        """unfollowing a user"""
        try:
            target_user = User.objects.get(id=user_id)
            if request.user == target_user:
                return Response(
                    {"detail": "You cannot unfollow yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if not target_user.followers.filter(id=request.user.id).exists():
                return Response(
                    {"detail": "You are not following this user."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            target_user.followers.remove(request.user)
            return Response(
                {"detail": f"You have unfollowed {target_user.username}."},
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


class FollowersListView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return User.objects.filter(following__id=user_id)


class FollowingListView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return User.objects.filter(followers__id=user_id)
