from django.urls import path,re_path
from .views import(
    home, create,
    profile,updateProfile,
    logout_view,
)

urlpatterns = [
    path('', home, name='home'),
    re_path(r'profile/(\d+)',profile,name = 'profile'),
    path('logout/', logout_view, name='logouts'),
    path('update/', updateProfile, name = 'updateProfile'),
    path('create/', create, name='create'),
    
]