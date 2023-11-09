from cake import views
from django.urls import path

urlpatterns = [
    path("api/cakes/", views.CakesView.as_view(), name="cakes"),
    path("api/cakes/<int:pk>/", views.CakeView.as_view(), name="cake"),
]
