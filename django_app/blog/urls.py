from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostEditView, PostDeleteView, post_like, post_detail, comment_like

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post-likes/<int:pk>/', post_like, name='post-likes'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment-likes/<int:pk>/', comment_like, name='comment-likes'),
    path('about/', views.about, name='blog-about'),
]

