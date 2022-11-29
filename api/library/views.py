from rest_framework import mixins
from rest_framework import generics
from .models import Livre

from .serializers import LivreSerializer
# Create your views here.

class LivreListCreate(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)