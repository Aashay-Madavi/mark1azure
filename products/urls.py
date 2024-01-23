from django.urls import path
from products import views
urlpatterns = [
    path('', views.AllProducts.as_view()),
    path('add/', views.AllProducts.as_view()),
    path('<int:pk>/', views.OneProduct.as_view()),
    path('edit/<int:pk>/', views.UpdateProduct.as_view()),
    path('delete/<int:pk>/', views.DeleteProduct.as_view())
]
