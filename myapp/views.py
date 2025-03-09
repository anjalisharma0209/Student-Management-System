from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Read (Retrieve all students)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

# Create (Add new student)
from django.shortcuts import render, redirect
from .forms import StudentForm

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list.html')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


# Update (Edit student)
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/edit_students.html', {'form': form})

# Delete (Remove student)
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'myapp/delete_students.html', {'students': student})