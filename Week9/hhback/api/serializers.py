from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)


    def create(self, validated_data):
        # {'name': 'new category 4'}
        # name='new category 4'
        company = Company(**validated_data)
        company.save()
        return company


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')
        # fields = '__all__'



class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = CompanySerializer(read_only=True)

    def create(self, validated_data):
        # {'name': 'new category 4'}
        # name='new category 4'
        vacancy = Vacancy(**validated_data)
        vacancy.save()
        return vacancy


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class VacancySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = CompanySerializer(read_only=True)


    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
        # fields = '__all__'