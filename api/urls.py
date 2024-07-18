from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, AllUserView, ImageListView, UploadImageView
urlpatterns = [
    # path('user', UserList.as_view(), name="user-list-view-create"),
    # path('user/<int:pk>', UserRUD.as_view(), name="user-update"),
    path('signup', RegisterView.as_view(), name="signup-user"),
    path('login', LoginView.as_view(), name="login-user"),
    path('user', UserView.as_view(), name="user-view"),
    path('logout', LogoutView.as_view(), name="logout-user"),
    path('userlist', AllUserView.as_view(), name="all-user-list"),
    path('imagelist', ImageListView.as_view(), name="image-list"),
    path('upload', UploadImageView.as_view(), name="upload-image"),
    # path('image/', ImageList.as_view()),
    # path('image/<int:pk>/', ImageDetail.as_view()),
]