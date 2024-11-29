from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save
from ..models import StudentBillPayment, StudentBill, Student, Bill, Semester, Account
from django.contrib.humanize.templatetags.humanize import intcomma


@receiver(post_save, sender=Student)
def create_student_bill(sender, instance, created, **kwargs):
    if created:
        print("Signal create_student_bill triggered")
        get_bill = Bill.objects.filter(name="Fee").first()
        get_semester = Semester.objects.filter(is_current=True).first()
        if get_semester:
            if get_bill is None:
                get_bill = Bill(name="Fee", amount=5000, semester=get_semester)
                get_bill.save()

            if instance.status not in  ["associate", "Associate"]:
                StudentBill.objects.create(
                    student=instance, bill=get_bill
                )
                print(f"Bill for {instance.user.first_name} {instance.user.last_name} created")


# during shift the year the bill will be created again
@receiver(post_save, sender=StudentBill)
def create_student_bill_payments(sender, instance, created, **kwargs):
    if created:
        print("Signal create_student_bill_payments triggered")
        StudentBillPayment.objects.create(
            student_bill=instance, amount=0
        )
        print(f"Payment for Bill {instance.student_bill.student} with amount {instance.amount} created")


@receiver(post_save, sender=StudentBillPayment)
def check_payment_logs_update_student_bill(sender, instance, created, **kwargs):
    if created:
        print("Signal check_payment_logs_update_student_bill triggered")
        get_student_bill = StudentBill.objects.filter(id=instance.student_bill.id).first()
        get_total_paid_amount = StudentBillPayment.objects.filter(student_bill=get_student_bill).aggregate(
            total_amount=Sum('amount'))['total_amount']

        if get_total_paid_amount >= get_student_bill.bill.amount:
            get_student_bill.status = "paid"

        elif get_total_paid_amount < get_student_bill.bill.amount and get_total_paid_amount != 0:
            get_student_bill.status = "partial payment"

        elif get_total_paid_amount == 0:
            get_student_bill.status = "unpaid"

        get_student_bill.paid_amount = get_total_paid_amount
        get_student_bill.save()

        # credit main account to get summary of all collected amount
        get_main_account = Account.objects.filter(name__in=("main", "Main")).first()
        if get_main_account is None:
            get_main_account = Account(name="Main", balance=instance.amount)
            get_main_account.save()
        else:
            get_main_account.balance += instance.amount
            get_main_account.save()

        # create account for each bill to keep summary of all amount in each bill
        get_bill_account = Account.objects.filter(name=str(get_student_bill.bill.name)).first()
        if get_bill_account is None:
            get_bill_account = Account(name=str(get_student_bill.bill.name), balance=instance.amount)
            get_bill_account.save()
        else:
            get_bill_account.balance += instance.amount
            get_bill_account.save()
