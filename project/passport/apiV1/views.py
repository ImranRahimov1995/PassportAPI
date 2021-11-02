from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from passport.models import Customer, Passport
from .serializers import *

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class PassportListView(generics.ListAPIView):
    serializer_class = PassportSerializer
    queryset = Passport.objects.all()

class PassportDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PassportDetailSerializer
    queryset = Passport.objects.all()
    lookup_field = 'personal'
    permission_classes = [IsAuthenticated,]

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer_INC
    queryset = Customer.objects.all()
    lookup_field = 'phone'
    permission_classes = [IsAuthenticated,]


class JoinedCreateView(generics.CreateAPIView):
    serializer_class = PassportSerializer
    queryset = Passport.objects.all()
    permission_classes = [IsAuthenticated,]