from django.core.exceptions import ValidationError
from django.db import models

from . import Student, Semester, User


class Bill(models.Model):
    name = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        db_table = 'bill'
        unique_together = (('semester', 'name'),)

    def save(self, *args, **kwargs):
        # Check if is_current is set to True
        if self.name:
            # Look for an existing semester with is_current=True
            existing_current = Bill.objects.filter(
                name=str(self.name), semester=self.semester
            ).exclude(pk=self.pk).exists()

            if existing_current:
                raise ValidationError("Semester {self.semester} with the name {self.name} already registered")

        # Save the semester
        super().save(*args, **kwargs)


class StudentBill(models.Model):
    STATUS = (
        ("unpaid", "unpaid"),
        ("partial payment", "partial payment"),
        ("paid", "paid")
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(default="unpaid", max_length=20, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student}-{self.bill}'

    class Meta:
        db_table = 'student_bill'
        unique_together = (('student', 'bill'),)


class StudentBillPayment(models.Model):
    METHOD = (
        ('Cash', 'Cash'),
        ('Mobile', 'Mobile'),
        ('Bank', 'Bank'),
    )
    student_bill = models.ForeignKey(StudentBill, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method = models.CharField(max_length=10, choices=METHOD, default="Cash")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Bill-{self.student_bill}: paid-{self.amount}'

    class Meta:
        db_table = 'student_bill_payment'


class Account(models.Model):
    name = models.CharField(max_length=60)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'account'
