from django.urls import path
from .views import profile, profile_edit, profile_delete

urlpatterns = [
    path('<int:pk>/', profile, name='profile'),
    path('<int:pk>/edit/', profile_edit, name='profile-edit'),
    path('<int:pk>/delete/', profile_delete.as_view(), name='profile-delete'),
]
