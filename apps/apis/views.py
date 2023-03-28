from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .models import Cotisation
from .serializers import ClientSerializer
from .serializers import CotisationSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class CotisationList(generics.ListCreateAPIView):
    queryset = Cotisation.objects.all()
    serializer_class = CotisationSerializer
    permission_classes = [IsAuthenticated]

class CotisationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cotisation.objects.all()
    serializer_class = CotisationSerializer
    permission_classes = [IsAuthenticated]
