from django.urls import path
from users import views
urlpatterns = [
    path('', views.AllUsers.as_view()),
    path('add/', views.AllUsers.as_view()),
    path('<int:id>/', views.OneUser.as_view()),
    path('edit/<int:id>/', views.UpdateUser.as_view()),
    path('delete/<int:id>/', views.DeleteUser.as_view()),


]
