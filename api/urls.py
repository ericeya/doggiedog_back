from django.urls import path
from .views import RegisterView, UserList, UserRUD

urlpatterns = [
    path('user/', UserList.as_view(), name="user-list-view-create"),
    path('user/<int:pk>', UserRUD.as_view(), name="user-update"),
    path('register', RegisterView.as_view(), name="register-user")
    # path('image/', ImageList.as_view()),
    # path('image/<int:pk>/', ImageDetail.as_view()),
]