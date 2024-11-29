from sqlite3 import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import save_student
from ..forms import BillForm, StudentPaymentForm
from ..models import Bill, Semester, StudentBill, StudentBillPayment, Account, Student
from django.contrib.humanize.templatetags.humanize import intcomma

@login_required(login_url='/')
def bills(request):
    template = 'registration/bills.html'
    get_bills = Bill.objects.all().order_by('name')
    get_semester = Semester.objects.filter(is_current=True).first()

    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            try:
                get_form = form.save(commit=False)
                get_form.name = "Fee"
                get_form.semester = get_semester
                get_form.save()

                message = 'Bill saved successfully'
                messages.success(request, message)
            except ValidationError as e:
                message = f'{e}'
                messages.error(request, message)
        else:
            message = 'Bill not saved please make sure you enter valid data and note bill type is unique per semister'
            messages.error(request, message)

        return redirect('bills')

    context = {
        'bills': get_bills,
        'form': BillForm,
    }

    return render(request, template, context)


@login_required(login_url='/')
def student_bills(request):
    template = 'registration/student-bills.html'
    get_student_bills = StudentBill.objects.all()

    context = {
        'student_bills': get_student_bills,
        'StudentPaymentForm': StudentPaymentForm
    }
    return render(request, template, context)


@login_required(login_url='/')
def student_bill_payments(request):
    template = 'registration/student-bill-payments.html'
    get_student_bill_payments = StudentBillPayment.objects.all()

    context = {
        'student_bill_payments': get_student_bill_payments,
    }
    return render(request, template, context)


@login_required(login_url='/')
def accounts(request):
    template = 'registration/accounts.html'
    get_account = Account.objects.all()

    context = {
        'accounts': get_account,
    }
    return render(request, template, context)

@login_required(login_url='/')
def save_payment(request):
    if request.method == "POST":
        form = StudentPaymentForm(request.POST)
        if form.is_valid():
            get_student_bill_id = request.POST['student_bill_id']
            get_student_bill = StudentBill.objects.get(pk=get_student_bill_id)
            get_amount = form.cleaned_data['amount']
            get_method = form.cleaned_data['method']

            save_student_payment = StudentBillPayment(
                student_bill = get_student_bill,
                amount = get_amount,
                method = get_method
            )
            save_student_payment.save()

            message = 'Payment saved successfully'
            messages.success(request, message)

            return redirect('student_bills')


@login_required(login_url='/')
def generate_bill(request):
    if request.method == "POST":
        get_bill_id = request.POST['bill_id']
        get_bill = Bill.objects.get(pk=get_bill_id)
        student_bill = StudentBill.objects.filter(bill=get_bill).values('student_id')
        get_student = Student.objects.exclude(id__in=student_bill).exclude(status="associate")

        for student in get_student:
            StudentBill.objects.create(
                student = student,
                bill = get_bill,
            )

            messages.success(request, 'Student bills created successfully.')

        return redirect(bills)