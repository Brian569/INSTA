from django.urls import path
from .views import(
    home,
    my_profile,
    comments, 
    login,
    register,
    logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('profile/', my_profile, name='profile'),
    path('comments/', comments, name='comments'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('logout/', logout_view, name='logouts')
]