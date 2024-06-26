from django.urls import path
from .views import RegisterUserView, LogoutUserView, LoginUserView, ListUsersView

urlpatterns = [
    path('register/',  RegisterUserView.as_view(), name = "register"),
    path('login/', LoginUserView.as_view(), name= "login"),
    path('logout/', LogoutUserView.as_view(), name = "logout"),
    path('list/', ListUsersView.as_view(), name = "users list"),
]