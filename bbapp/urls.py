from django.urls import path
from .views import PostView, IndexView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostView.as_view(), name='post'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
