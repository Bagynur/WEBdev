import json
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company doesn`t exist'})
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({}, status=204)

@csrf_exempt
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
@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': 'Vacancy doesn`t exist'})
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = VacancySerializer(instance=vacancy, data=data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({}, status=204)

@csrf_exempt
def vacancy_list10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all().filter(salary__gte=2.0).order_by('-salary')[:11:1]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)