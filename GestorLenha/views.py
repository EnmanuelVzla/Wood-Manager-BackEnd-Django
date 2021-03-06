from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from GestorLenha.models import *
from GestorLenha.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user, 
               context={'request': request})
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        elif self.action in ['create']:
            self.permission_classes = [permissions.AllowAny, ]
        return super().get_permissions()

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class encomendas_view(viewsets.ModelViewSet):
    queryset = Encomenda.objects.all()
    serializer_class = EncomendaSerializer
    permission_classes = [permissions.AllowAny]
    filter_fields = ["cliente", "estado", "is_deleted"]


class config_view(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    permission_classes = [permissions.IsAuthenticated]