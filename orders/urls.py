from django.urls import path
from orders.views import AllOrders, OneOrder, UpadteOrder, AddOrder, DeleteOrder
urlpatterns = [
    path('', AllOrders.as_view()),
    path('add/', AddOrder.as_view()),
    path('myorders/', OneOrder.as_view()),
    path('edit/<int:id>/', UpadteOrder.as_view()),
    path('delete/<int:id>/', DeleteOrder.as_view()),
]
