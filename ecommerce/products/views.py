from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Person
from .forms import ProductForm
from .forms import PersonForm
from .models import Student


# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def post_product_data(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/addProduct.html', context)


def get_product(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        context = {
            'name': name,
            'price': price
        }
    else:
        context = {
            'name': 'NULL',
            'price': 'NULL'
        }
    return render(request, 'products/getProduct.html', context)


def post_person_data(request):
    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, 'products/addPerson.html', context)


def post_student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        batch = data['batch']
        image_url = data['image_url']
        category = data['category']
        student = Student.objects.create(firstname=firstname, lastname=lastname,
                                         batch=batch, image_url=image_url,
                                         category=category)
        if student:
            return redirect('/products/getStudent')
        else:
            return HttpResponse('Student cannot be added')

    return render(request, 'products/addStudent.html')


def get_student(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'activate_student': 'active'
    }
    return render(request, 'products/showStudent.html', context)


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.firstname = request.POST['firstname']
        student.lastname = request.POST['lastname']
        student.batch = request.POST['batch']
        student.category = request.POST['category']
        student.image_url = request.POST['image_url']
        student.save()
        return redirect('/products/getStudent')
    context = {
        'student': student
    }
    return render(request, 'products/updateStudent.html', context)


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/getStudent')


def show_person_mf(request):
    person = Person.objects.all()
    context = {
        'person': person,
        'activate_personMF': 'active'
    }
    return render(request, 'products/showPersonMF.html', context)


def post_person_mf(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/getPersonMF')

    context = {
        'form': PersonForm
    }
    return render(request, 'products/postPersonMF.html', context)


def deletePersonMF(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('/products/getPersonMF')