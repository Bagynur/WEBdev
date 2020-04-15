from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2

@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})


def vacancy_from_company(request, company_id):
    if request.method == "GET":
        try:
            vacancy_list = Vacancy.objects.all()
            vacancies = []
            for vacancy in vacancy_list:
                if vacancy.company.id == company_id:
                    vacancies.append(vacancy.to_vacancy_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': 'company doesn`t exist'})
        return JsonResponse(vacancies,safe=False)
    elif request.method == "POST":
        pass

    # vacancies = Vacancy.objects.all()
    # vacancy = []
    # for vac in vacancies:
    #     a = vac.to_vacancy_json()
    # if a['company_id'] == company_id:
    #     vacancy.append(a)
    # if len(vacancy):
    #     return JsonResponse(vacancy, safe=False)
    # else:
    #     return HttpResponse("Error I cannot found smthg")
@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'deleted': True})

@api_view(['GET'])
def vacancy_list10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all().filter(salary__gte=2.0).order_by('-salary')[:11:1]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)