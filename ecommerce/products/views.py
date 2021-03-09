from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Person, FileUpload
from .forms import ProductForm, FileForm
from .forms import PersonForm
from .models import Student
import os
from django.contrib import messages


# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'activate_product': 'active'
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


def get_person_mf(request):
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
            messages.add_message(request, messages.SUCCESS, 'Person Added Successfully')
            return redirect('/products/getPersonMF')
        else:
            messages.add_message(request, messages.ERROR, 'Please provide correct details')
            return render(request, 'products/addPersonMF.html',{'form':form})

    context = {
        'form': PersonForm,
        'activate_personMF': 'active'
    }
    return render(request, 'products/addPersonMF.html', context)


def delete_person_mf(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('/products/getPersonMF')


def update_person_mf(request, person_id):
    instance = Person.objects.get(id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/products/getPersonMF')
        context = {
            'form': PersonForm(instance=instance),
            'active_personMF': 'active'
        }
        return render(request, 'products/updatePersonMF.html', context)


def post_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        file_obj = FileUpload(title=title, file=file)
        file_obj.save()
        if file_obj:
            return redirect('/products/getFile')
        else:
            return HttpResponse("File cannot be add")

    context = {
        'activate_file': 'active'
    }
    return render(request, 'products/addFile.html', context)


def get_file(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_file': 'active'
    }
    return render(request, 'products/showFile.html', context)


def update_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == 'POST':
        if request.FILES.get('file'):
            file.title = request.POST.get('title')
            file.file = request.FILES.get('file')
            file.save()
        else:
            file.title = request.POST.get('title')
            file.save()

        return redirect('/products/getFile')
    context = {
        'file': file,
        'activate_file': 'active'

    }
    return render(request, 'products/updateFile.html',context)


def delete_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/products/getFileMF')


def get_file_mf(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_fileMF': 'active'
    }
    return render(request, 'products/showFileMF.html', context)


def post_file_mf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')
    context = {
        'form': FileForm,
        'active_fileMF': 'active'
    }
    return render(request, 'products/addFile.html', context)


def delete_file_mf(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    os.remove(file.file.path)
    file.delete()
    return redirect('/products/getFileMF')


def update_file_mf(request, file_id):
    instance = FileUpload.objects.get(id=file_id)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')

    context = {
        'form': FileForm(instance=instance),
        'activate_fileMF': 'active'
    }
    return render(request, 'products/updateFileMF.html', context)



