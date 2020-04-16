from django.urls import path

from api.views import company_list, company_detail, vacancy_list, vacancy_detail, vacancy_from_company, vacancy_list10

from rest_framework_jwt.views import obtain_jwt_token

from api.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView,VacancyDetailAPIView


urlpatterns = [

    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>', CompanyDetailAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>', vacancy_detail),
    path('companies/<int:company_id>/vacancies', vacancy_from_company),
    path('vacancies/top_ten', vacancy_list10)

]