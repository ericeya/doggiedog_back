from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
urlpatterns = [
    # path('user', UserList.as_view(), name="user-list-view-create"),
    # path('user/<int:pk>', UserRUD.as_view(), name="user-update"),
    path('register', RegisterView.as_view(), name="register-user"),
    path('login', LoginView.as_view(), name="login-user"),
    path('user', UserView.as_view(), name="user-view"),
    path('logout', LogoutView.as_view(), name="logout-user")
    # path('image/', ImageList.as_view()),
    # path('image/<int:pk>/', ImageDetail.as_view()),
]