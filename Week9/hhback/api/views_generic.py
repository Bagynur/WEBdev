from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Company, Vacancy

from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    # permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    # permission_classes = (IsAuthenticated,)

class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer2


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer2