from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.shortcuts import render, redirect
import csv
from ..function import check_balance, send_sms_to_student
from ..models import Student, Programme, Committee, StudentCommittee, User, Position
from ..forms import StudentForm, CommitteeForm, MessageForm, PositionForm, StudentUploadForm, \
    SelfStudentRegistrationForm


@login_required(login_url='/')
def students(request):
    template = 'registration/student.html'
    get_students = Student.objects.filter(status__in=("finalist", "continuing")).order_by('programme__abb')
    get_finalist_students = Student.objects.filter(status="finalist").count()
    get_continuing_students = Student.objects.filter(status="continuing").count()
    get_associate_students = Student.objects.filter(status="associate").count()
    sms_balance = check_balance()

    try:
        sms_balance_value = sms_balance['data']['credit_balance']
    except:
        sms_balance_value = 0

    context = {
        'StudentUploadForm': StudentUploadForm,
        'students': get_students,
        'form': StudentForm,
        'MessageForm': MessageForm,
        'sms_balance': sms_balance_value,
        'get_finalist_students': get_finalist_students,
        'get_continuing_students': get_continuing_students,
        'get_associate_students': get_associate_students,
        'all_member': get_associate_students + get_finalist_students + get_continuing_students,
    }
    return render(request, template, context)


def self_student_registration(request):
    context = {
        'SelfStudentRegistrationForm': SelfStudentRegistrationForm,
    }
    template = 'auth/self-student-registration.html'
    return render(request, template, context)


@login_required(login_url='/')
def filter_member(request, status):
    get_filtered_students = Student.objects.filter(status=status)
    sms_balance = check_balance()

    try:
        sms_balance_value = sms_balance['data']['credit_balance']
    except:
        sms_balance_value = 0

    context = {
        'students': get_filtered_students,
        'status': status,
        'form': StudentForm,
        'MessageForm': MessageForm,
        'sms_balance': sms_balance_value,
    }

    template = 'registration/filter-student.html'
    return render(request, template, context)


@login_required(login_url='/')
def associate(request):
    template = 'registration/associate.html'
    get_associates = Student.objects.filter(is_associate=True).order_by('programme__abb')
    context = {
        'associates': get_associates,
    }
    return render(request, template, context)


@login_required(login_url='/')
def send_sms_to_students(request):
    get_students = Student.objects.filter(is_associate=False)

    batch_size = 100
    total_students = get_students.count()
    start_index = 0
    count = 1

    if request.method == "POST":
        message = request.POST.get('message')
        if message:
            while start_index < total_students:
                end_index = start_index + batch_size
                batch_students = get_students[start_index:end_index]
                for student in batch_students:
                    phone = f'255{student.user.phone[1:]}'
                    try:
                        # print("Hello word")
                        send_sms_to_student(message, phone)
                        count = count + 1
                    except:
                        pass
                start_index = end_index

    message = f"Message sent to {count - 1} students"
    messages.success(request, message)
    return redirect('students')


@login_required(login_url='/')
def student_committee(request):
    template = 'registration/student-committee.html'
    get_students = StudentCommittee.objects.filter().order_by('student')
    get_committees = StudentCommittee.objects.exclude(
        student__status="associate"
    ).values("committee__name").annotate(total_committee=Count("committee"))

    print(get_committees)

    context = {
        'students': get_students,
        'committees': get_committees,
    }
    return render(request, template, context)


@login_required(login_url='/')
def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        try:
            get_student = Student.objects.get(id=student_id)
            get_user = User.objects.get(id=get_student.user.id)

            get_student.delete()
            get_user.delete()

            message = "Student saved successfully"
            messages.success(request, message)

        except:
            message = "Something went wrong Try again"
            messages.error(request, message)

        return redirect('students')


@login_required(login_url='/')
def save_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            level = request.POST.get('level')
            phone = request.POST.get('phone')

            get_user_instance = form.save(commit=False)

            get_user_instance.password = make_password(f'{last_name}'.lower())
            get_user_instance.username = f'{first_name}.{last_name}'.lower()
            get_user_instance.save()

            get_programme = Programme.objects.get(id=request.POST.get('programme'))
            get_committee = Committee.objects.get(id=request.POST.get('committee'))

            # save student committee
            save_student_instance = Student(
                user=get_user_instance,
                programme=get_programme
            )

            save_student_instance.save()

            # save student committee
            save_student_committee = StudentCommittee(
                student=save_student_instance,
                committee=get_committee
            )
            save_student_committee.save()

            # send message to student that registered successfully
            phone = f'255{phone[1:]}'
            message = f"Congratulation {first_name.title()} {last_name.title()} you have been successfully registered to" \
                      f" CCT USCF Mzumbe"

            # check if message not sent to student the handle the error
            try:
                send_sms_to_student(message, phone)
                message = "Student saved successfully and registration message sent"
            except:
                message = "Student saved successfully but registration message not sent"

            messages.success(request, message)
            return redirect('students')
        else:
            message = "Student not saved successfully"
            messages.error(request, message)
            return redirect('students')


@login_required(login_url='/')
def committee(request):
    template = 'registration/committee.html'
    get_committees = Committee.objects.all().order_by('name')
    edit_committee_forms = {cot.id: CommitteeForm(instance=cot) for cot in get_committees}

    if request.method == "POST":
        form = CommitteeForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Committee saved successfully"
            messages.success(request, message)
        else:
            message = "Committee not saved successfully"
            messages.error(request, message)

    context = {
        'committee': get_committees,
        'cf': CommitteeForm,
        'edit_committee_forms': edit_committee_forms
    }

    return render(request, template, context)


@login_required(login_url='/')
def update_committee(request):
    if request.method == 'POST':
        try:
            committee_id = request.POST.get('committee_id')
            get_committee = Committee.objects.get(id=committee_id)
            form = CommitteeForm(request.POST, instance=get_committee)
            if form.is_valid():
                form.save()
                message = f'Committee updated successfully'
                messages.success(request, message)
            else:
                message = f'Somthing went wrong try again'
                messages.error(request, message)
        except:
            message = f'Something went wrong try again'
            messages.error(request, message)
    return redirect('committee')


@login_required(login_url='/')
def position(request):
    template = 'registration/position.html'
    get_positions = Position.objects.all().order_by('-name')
    edit_position_forms = {pos.id: PositionForm(instance=pos) for pos in get_positions}

    if request.method == 'POST':
        position_form = PositionForm(request.POST)
        if position_form.is_valid():
            get_form = position_form.save(commit=False)

            name = request.POST.get('name')
            get_form.name = f'{name}'.upper()
            try:
                get_form.save()
                message = 'Position saved successfully'
                messages.success(request, message)
            except:
                message = f'Position name is unique'
                messages.error(request, message)
        else:
            message = f'Position not saved please make sure you enter valid data'
            messages.error(request, message)
        return redirect('positions')
    context = {
        'title': 'Position',
        'positions': get_positions,
        'form': PositionForm,
        'edit_position_forms': edit_position_forms
    }
    return render(request, template, context)


@login_required(login_url='/')
def update_position(request):
    if request.method == 'POST':
        position_id = request.POST.get('position_id')
        position_instance = Position.objects.get(id=position_id)
        form = PositionForm(request.POST, instance=position_instance)

        if form.is_valid():
            try:
                form.save()
                message = 'Position updated successfully'
                messages.success(request, message)
            except:
                message = f'Position name is unique'
                messages.error(request, message)
        else:
            message = 'Position not updated please make sure you enter valid data'
            messages.error(request, message)

    return redirect('positions')


@login_required(login_url='/')
def delete_position(request):
    if request.method == 'POST':
        position_id = request.POST.get('position_id')
        try:
            position_instance = Position.objects.get(id=position_id)
            position_instance.delete()
            message = 'Position deleted successfully'
            messages.success(request, message)
        except:
            message = 'Position with give name not found'
            messages.error(request, message)

        return redirect('positions')


def upload_student(request):
    if request.method == 'POST':
        form = StudentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            # Ensure it's a CSV file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a CSV file.')
                return redirect('upload_student')

            # Decode the uploaded file and parse it
            data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(data)
            next(reader, None)  # Skip the header row if there is one

            for row in reader:
                # id	first_name	middle_name	last_name	sex	phone	programme_id
                try:
                    user_id, first_name, middle_name, last_name, sex = row[0], row[1], row[2], row[3], row[4]
                    phone, programme_id = row[5], row[6]
                    year = datetime.now().year
                    username = f"{first_name.lower()}.{last_name.lower()}"
                    email = f"{username}{year}@uscfmzumbe.ac.tz"

                    get_programme = Programme.objects.get(id=programme_id)
                    save_user = User(
                        id=user_id,
                        first_name=first_name,
                        middle_name=middle_name or "",
                        last_name=last_name,
                        sex=sex,
                        phone=phone,
                        email=email,
                        username=username
                    )
                    save_user.save()

                    save_new_student = Student(
                        user=save_user,
                        programme=get_programme,
                    )
                    save_new_student.save()

                except Exception as e:
                    messages.error(request, f"Error processing row {row}: {e}")
                    continue  # Skip to the next row if there's an error

            messages.success(request, 'Students uploaded successfully.')
        else:
            messages.error(request, f"Error {form.errors}")
    return redirect('students')
