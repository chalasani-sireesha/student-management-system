from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
from django.contrib import messages 
from django.core.paginator import Paginator
def home(request):
    return render(request, 'home.html')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully !")
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})
def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    
    paginator = Paginator(students, 5)   # 5 students per page

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'student_list.html', {
        'page_obj':page_obj,
        'query':query
        
    })

   
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})

# Create your views here.
