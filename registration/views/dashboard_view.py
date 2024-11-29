from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from ..models import Student


@login_required(login_url='/')
def dashboard(request):
    template = 'registration/dashboard.html'
    faculty_summary = Student.objects.filter(status__in=("continuing", "finalist")).values_list('programme__department__unit__abb').annotate(
        total_student=Count('user'))

    gender_summary = Student.objects.filter(status__in=("continuing", "finalist")).values_list('user__sex').annotate(student=Count('user__sex'))

    context = {
        'faculty_summary': faculty_summary,
        'gender_summary': gender_summary
    }
    return render(request, template, context)
