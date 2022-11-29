from django.urls import path

from .views import LivreListCreate, CategoryListCreate

urlpatterns = [
    path('', LivreListCreate.as_view()),
    path('category/', CategoryListCreate.as_view())
]
