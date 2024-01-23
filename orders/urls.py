from django.urls import path
from orders.views import AllOrders, OneOrder, UpadteOrder, DeleteOrder
urlpatterns = [
    path('', AllOrders.as_view()),
    path('add/', AllOrders.as_view()),
    path('<int:id>/', OneOrder.as_view()),
    path('edit/<int:id>/', UpadteOrder.as_view()),
    path('delete/<int:id>/', DeleteOrder.as_view()),
]
