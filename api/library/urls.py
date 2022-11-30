from django.urls import path

from .views import *

urlpatterns = [
    path('', LivreListView.as_view()),
    path('detail/<int:id>', LivreRetrieveView.as_view()),
    path('update/<int:id>', LivreUpdateView.as_view()),
    path('delete/<int:id>', LivreDeleteView.as_view()),
    path('create/', LivreCreateView.as_view()),
    path('category/list/', CategoryListView.as_view()),
    path('category/retrieve/<int:id>', CategoryRetrieveView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/update/<int:id>', CategoryUpdateView.as_view()),
    path('category/delee/<int:id>', CategoryDeleteView.as_view())
]
