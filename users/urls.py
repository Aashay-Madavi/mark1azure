from django.urls import path
from users import views
urlpatterns = [
    path('', views.FetchUsers.as_view()),
    path('register/', views.AllUsers.as_view()),
    path('<int:id>/', views.FetchUser.as_view()),
    path('edit/<int:id>/', views.UpdateUser.as_view()),
    path('delete/<int:id>/', views.DeleteUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.LogoutUser.as_view()),



]
