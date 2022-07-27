from django.shortcuts import render
from People.models import People

# Create your views here.


def hola(request):
    return render(request,'primer_template.html' , context={})

def add_person(request):
    # person_1 = People.objects.create(name = 'Lucila', last_name = 'Werner', age = 34, DOB = '1987-09-22', relationship = 'Mother')
    # person_2 = People.objects.create(name = 'Michael', last_name = 'Arduino', age = 3, DOB = '2018-08-17', relationship = 'Son')
    # person_3 = People.objects.create(name = 'Pedro', last_name = 'Arduino', age = 33, DOB = '1989-05-17', relationship = 'Father')
    # person_4 = People.objects.create(name = 'Lucila', last_name = 'Arduino', age = 6, DOB = '2016-03-18', relationship = 'Daughter')
    
    # listper = {
    #     'person':[person_1, person_2, person_3, person_4]
    # }
    
    persona = People.objects.all()
    return render (request,'new_person.html' , context={'listper': persona})
    