from django.urls import path
from .views import(
    home,
    my_profile,
    user_profile,
    edit_profile,
    comments
)

urlpatterns = [
    path('', home, name='home'),
    path('profile/', my_profile, name='profile'),
    path('user_profile/', user_profile, name='user_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('comments', comments, name='comments')
]