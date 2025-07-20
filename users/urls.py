from django.urls import path
from .views import LogoutView, UserRegisterView, ActivateUserView, LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('activate/<int:uid>/<str:token>/', ActivateUserView.as_view(), name='user-activate'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
