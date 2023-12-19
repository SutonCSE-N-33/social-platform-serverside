
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#for API
from rest_framework import routers
from accounts.views import (
    LoginAPIView,
    RegistrationAPIView,
    LogoutView,
    DeleteUserView
)
from post.views import PostViewSet, PostDetailViewSet
from comment.views import CommentViewSet
from reply.views import ReplyViewSet
from react.views import ReactViewSet
from notification.views import NotificationViewSet, CountNotificationViewSet


router = routers.DefaultRouter()
router.register(r"post",PostViewSet)
router.register(r"postDetails",PostDetailViewSet, basename="id")
router.register(r'comment',CommentViewSet)
router.register(r'react',ReactViewSet)
router.register(r'reply',ReplyViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'count_Notification', CountNotificationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path('',include(router.urls)),
    path("alluser/delete/<int:id>", DeleteUserView.as_view(), name="user_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
