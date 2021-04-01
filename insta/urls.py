from django.urls import path
from .views import(
    home,
    my_profile,
    comments, 
    login,
    register
)

urlpatterns = [
    path('', home, name='home'),
    path('profile/', my_profile, name='profile'),
    path('comments/', comments, name='comments'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register')
]