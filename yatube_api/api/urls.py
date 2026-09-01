from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns_v1 = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='post-comments-list'),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view(
             {'get': 'retrieve',
              'put': 'update',
              'patch': 'partial_update',
              'delete': 'destroy'}), name='post-comments-detail'),
    path('api-token-auth/', views.obtain_auth_token),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]
