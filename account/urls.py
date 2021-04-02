from django.contrib.auth import views as auth_views
from django.urls import path

from account.views import RegisterView, ActivationView, user_modify

urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activation'),
    path('modify/<int:pk>', user_modify, name='user_modify'),
]
