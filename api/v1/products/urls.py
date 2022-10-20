from django.urls import path
from api.v1.products import views

urlpatterns = [
    path('', views.products),
    path('view/<int:pk>', views.product)
]
