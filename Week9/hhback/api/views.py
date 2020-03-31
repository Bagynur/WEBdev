from django.http.response import HttpResponse, JsonResponse

from api.models import Company, Vacancy


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        company_json = [company.to_company_json() for company in companies]
        return JsonResponse(company_json, safe=False)
    elif request.method == 'POST':
        # Must create new Product from request body
        pass


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company doesn`t exist'})
    if request.method == 'GET':
        return JsonResponse(company.to_company_json())
    elif request.method == 'PUT':
    # update product object
        pass
    elif request.method == 'DELETE':
    # delete selected object
        pass


def vacancy_from_company(request, company_id):
        vacancy = Company.objects.all()
        len_vacancy = len(vacancy)
        vacancy = []
        for i in range(len_vacancy):
            if vacancy[i].company_id_id.id == company_id:
                vacancy.append(vacancy[i])
        vacancy_json = [x.to_vacancy_json() for x in vacancy]
        if (len(vacancy_json) != 0):
            return JsonResponse(vacancy_json, safe=False)
        else:
            return JsonResponse({'error': 'Company doesn`t exist'})


def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancy_json = [vacancy.to_vacancy_json() for vacancy in vacancies]
        return JsonResponse(vacancy_json, safe=False)
    elif request.method == 'POST':
        # Must create new Product from request body
        pass


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': 'Vacancy doesn`t exist'})
    if request.method == 'GET':
        return JsonResponse(vacancy.to_vacancy_json())
    elif request.method == 'PUT':
    # update product object
        pass
    elif request.method == 'DELETE':
    # delete selected object
        pass

def vacancy_list10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
        vacancy_json = [vacancy.to_vacancy_json() for vacancy in vacancies]
        return JsonResponse(vacancy_json, safe=False)
