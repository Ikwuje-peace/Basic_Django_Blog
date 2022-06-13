from django.urls import path
from .views import HomeView, CreatePostView, PostDetailView, EditPostView, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('create_post/', CreatePostView.as_view(), name = 'new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'details'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name= 'edit'),
    path('post/delete/<int:pk>', DeletePost.as_view(), name='delete'),
]
