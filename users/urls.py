from django.urls import path
from users.views import (UserLOginView, logout_view, profile_view, CreateUserView, UserProfileView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('login/', UserLOginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('registration/',CreateUserView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()),name = 'edit_profile'),

]