from django.urls import path, include
from .views import BlogViewSet,UserViewSet,RegisterView, LoginView,CommentViewSet
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

from .views import CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]