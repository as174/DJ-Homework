from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_list = Student.objects.all()
    context = {'object_list': student_list}

    return render(request, template, context)
