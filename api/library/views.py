from rest_framework import generics, permissions, authentication
from .models import Category, Livre

from .serializers import CategorySerializer, LivreSerializer
# Create your views here.

"""
Ceci sont les vue concernant les category
"""
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]



class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]



"""
Ceci sont les vue concernant les Livre
"""
class LivreCreateView(generics.CreateAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer




class LivreListView(generics.ListAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class LivreRetrieveView(generics.RetrieveAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer



class LivreUpdateView(generics.UpdateAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    

class LivreDeleteView(generics.DestroyAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer