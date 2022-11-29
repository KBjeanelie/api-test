from django.urls import path

from .views import LivreListCreate

urlpatterns = [
    path('', LivreListCreate.as_view())
]
