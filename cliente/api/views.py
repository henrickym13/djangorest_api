from rest_framework import viewsets
from cliente.api.serializers import ClienteSerializer
from cliente.models import Cliente


class ClienteViews(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
