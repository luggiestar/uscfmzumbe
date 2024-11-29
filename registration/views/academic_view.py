from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from ..forms import UnitForm, DepartmentsForm, ProgrammeForm, YearForm, SemesterForm
from ..models import Unit, Department, Programme, Year, Semester


@login_required(login_url='/')
def unit(request):
    template = 'registration/unit.html'
    get_units = Unit.objects.all().order_by('name')
    edit_unit_forms = {units.id: UnitForm(instance=units) for units in get_units}

    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            try:
                get_form = form.save(commit=False)
                get_form.name = str(request.POST['name']).upper()
                get_form.abb = str(request.POST['abb']).upper()
                get_form.save()

                message = 'Unit saved successfully'
                messages.success(request, message)
            except:
                message = f'Unit name is unique'
                messages.error(request, message)
        else:
            message = 'Unit not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('unit')

    context = {
        'title': 'Units',
        'units': get_units,
        'form': UnitForm,
        'edit_unit_forms': edit_unit_forms
    }

    return render(request, template, context)


@login_required(login_url='/')
def update_unit(request):
    if request.method == 'POST':
        unit_id = request.POST.get('unit_id')
        unit_instance = Unit.objects.get(id=unit_id)
        form = UnitForm(request.POST, instance=unit_instance)
        if form.is_valid():
            try:
                form.save()
                message = 'Unit updated successfully'
                messages.success(request, message)
            except:
                message = f'Unit name is unique'
                messages.error(request, message)
        else:
            message = f'{form.errors}Unit not updated please make sure you enter valid data'
            messages.error(request, message)

    return redirect('unit')


@login_required(login_url='/')
def delete_unit(request):
    try:
        unit_id = request.POST.get('unit_id')
        unit_instance = Unit.objects.get(id=unit_id)
        unit_instance.delete()

        message = f'Unit Deleted successfully'
        messages.success(request, message)
        return redirect('unit')
    except:
        message = f'Unit does not exist'
        messages.error(request, message)
        return redirect('unit')


@login_required(login_url='/')
def department(request):
    template = 'registration/department.html'
    get_departments = Department.objects.all().order_by('unit')
    edit_department_forms = {depart.id: DepartmentsForm(instance=depart) for depart in get_departments}

    if request.method == "POST":
        form = DepartmentsForm(request.POST)
        if form.is_valid():
            try:
                get_form = form.save(commit=False)
                get_form.name = str(request.POST['name']).upper()
                get_form.abb = str(request.POST['abb']).upper()
                get_form.save()

                message = 'department saved successfully'
                messages.success(request, message)
            except:
                message = f'department name is unique'
                messages.error(request, message)
        else:
            message = 'department not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('department')

    context = {
        'title': 'Departments',
        'departments': get_departments,
        'form': DepartmentsForm,
        'edit_department_forms': edit_department_forms
    }

    return render(request, template, context)


@login_required(login_url='/')
def update_department(request):
    if request.method == 'POST':
        try:
            department_id = request.POST.get('department_id')
            get_departments = Department.objects.get(id=department_id)
            form = DepartmentsForm(request.POST, instance=get_departments)
            if form.is_valid():
                form.save()
                message = f'Department updated successfully'
                messages.success(request, message)
            else:
                message = f'Somthing went wrong try again {form.errors}'
                messages.error(request, message)
        except:
            message = f'Something went wrong try again'
            messages.error(request, message)
    return redirect('department')


@login_required(login_url='/')
def delete_department(request):
    try:
        department_id = request.POST.get('department_id')
        department_instance = Department.objects.get(id=department_id)
        department_instance.delete()

        message = f'Department Deleted successfully'
        messages.success(request, message)
    except:
        message = f'Department does not exist'
        messages.error(request, message)

    return redirect('department')


@login_required(login_url='/')
def programme(request):
    template = 'registration/programme.html'
    get_programmes = Programme.objects.all().order_by('level')
    edit_programme_forms = {prog.id: ProgrammeForm(instance=prog) for prog in get_programmes}

    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            try:
                get_form = form.save(commit=False)
                get_form.name = str(request.POST['name']).upper()
                get_form.abb = str(request.POST['abb']).upper()
                get_form.save()

                message = 'Programme saved successfully'
                messages.success(request, message)
            except:
                message = f'Something went wrong try again'
                messages.error(request, message)
        else:
            message = 'Programme not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('programme')

    context = {
        'title': 'Programme',
        'programmes': get_programmes,
        'form': ProgrammeForm,
        'edit_programme_forms': edit_programme_forms,
    }

    return render(request, template, context)


@login_required(login_url='/')
def update_programme(request):
    if request.method == 'POST':
        try:
            programme_id = request.POST.get('programme_id')
            get_programme = Programme.objects.get(id=programme_id)
            form = ProgrammeForm(request.POST, instance=get_programme)
            if form.is_valid():
                form.save()
                message = f'Programme updated successfully'
                messages.success(request, message)
            else:
                message = f'Somthing went wrong try again'
                messages.error(request, message)
        except:
            message = f'Something went wrong try again'
            messages.error(request, message)
    return redirect('programme')


@login_required(login_url='/')
def delete_programme(request):
    try:
        programme_id = request.POST.get('programme_id')
        programme_instance = Programme.objects.get(id=programme_id)
        programme_instance.delete()

        message = f'Programme Deleted successfully'
        messages.success(request, message)
    except:
        message = f'Programme does not exist'
        messages.error(request, message)

    return redirect('programme')


def year(request):
    template = 'registration/year.html'
    get_years = Year.objects.all().order_by('name')
    get_year = semester.objects.filter(is_current=True).first()

    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = 'Year saved successfully'
                messages.success(request, message)
            except:
                message = f'Year name is unique'
                messages.error(request, message)
        else:
            message = 'Year not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('years')

    context = {
        'title': 'Years',
        'years': get_years,
        'form': YearForm,
        'get_year': get_year,
    }
    return render(request, template, context)


@login_required(login_url='/')
def update_year(request):
    if request.method == 'POST':
        year_id = request.POST.get('year_id')
        year_instance = Year.objects.get(id=year_id)
        form = YearForm(request.POST, instance=year_instance)
        if form.is_valid():
            try:
                form.save()
                message = 'Year updated successfully'
                messages.success(request, message)
            except:
                message = f'Year name is unique'
                messages.error(request, message)
        else:
            message = f'{form.errors}Year not updated please make sure you enter valid data'
            messages.error(request, message)

    return redirect('year')


@login_required(login_url='/')
def set_semester_to_current(request):
    if request.method == 'POST':
        semester_id = request.POST.get('semester_id')
        current_semester_instance = semester.objects.filter(is_current=True).first()

        if current_semester_instance is not None:
            current_semester_instance.is_current = False
            current_semester_instance.save()

        try:
            semester_instance = semester.objects.get(id=semester_id)
            semester_instance.is_current = True
            semester_instance.save()

            message = f'{semester_instance} semester is active now'
            messages.success(request, message)
        except:
            message = f'Something went wrong try again'
            messages.error(request, message)
    else:
        message = f'Bad request'
        messages.error(request, message)

    return redirect('semester')


@login_required(login_url='/')
def delete_year(request):
    if request.method == 'POST':
        year_id = request.POST.get('year_id')
        try:
            year_instance = Year.objects.get(id=year_id)
            year_instance.delete()
            message = 'year deleted successfully'
            messages.success(request, message)
        except:
            message = 'Year with give name not found'
            messages.error(request, message)

        return redirect('year')


def semester(request):
    template = 'registration/semester.html'
    get_semesters = Semester.objects.all().order_by('name')
    edit_semester_forms = {sem.id: SemesterForm(instance=sem) for sem in get_semesters}
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = 'semester saved successfully'
                messages.success(request, message)
            except ValidationError as e:
                message = f'semester name is unique {str(e)}'
                messages.error(request, message)
        else:
            message = 'semester not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('semester')

    context = {
        'title': 'semesters',
        'semesters': get_semesters,
        'form': SemesterForm,
        'get_semester': get_semesters,
        'edit_semester_forms': edit_semester_forms
    }
    return render(request, template, context)


@login_required(login_url='/')
def update_semester(request):
    if request.method == 'POST':
        semester_id = request.POST.get('semester_id')
        semester_instance = Semester.objects.get(id=semester_id)
        form = SemesterForm(request.POST, instance=semester_instance)
        if form.is_valid():
            try:
                form.save()
                message = 'semester updated successfully'
                messages.success(request, message)
            except:
                message = f'semester name is unique'
                messages.error(request, message)
        else:
            message = f'{form.errors}semester not updated please make sure you enter valid data'
            messages.error(request, message)

    return redirect('semester')


@login_required(login_url='/')
def delete_semester(request):
    if request.method == 'POST':
        semester_id = request.POST.get('semester_id')
        try:
            semester_instance = Semester.objects.get(id=semester_id)
            semester_instance.delete()
            message = 'semester deleted successfully'
            messages.success(request, message)
        except:
            message = 'semester with give name not found'
            messages.error(request, message)

        return redirect('semester')
