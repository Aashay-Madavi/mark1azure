from django.urls import path
from .views import AddTrack, FetchOrderTrack, UpdateOrderTrack, DeleteOrderTrack, FetchAllOrderTrack
urlpatterns = [
    path('', FetchAllOrderTrack.as_view()),
    path('add/', AddTrack.as_view()),
    path('myorder/<int:id>/', FetchOrderTrack.as_view()),
    path('edit/<int:id>/', UpdateOrderTrack.as_view()),
    path('delete/<int:id>/', DeleteOrderTrack.as_view())
]
