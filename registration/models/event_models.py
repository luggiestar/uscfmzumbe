from django.core.exceptions import ValidationError
from django.db import models
from . import Semester, Student, Position


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    projection = models.DecimalField("Target amount", max_digits=10, decimal_places=2)
    committee_amount = models.DecimalField("Amount to be paid by committee", max_digits=10, decimal_places=2)
    member_amount = models.DecimalField("Amount to be paid by member",max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        db_table = 'event'


class EventCommittee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event}"

    class Meta:
        ordering = ['event']
        verbose_name = 'Event Committee'
        verbose_name_plural = 'Event Committee'
        db_table = 'event_committee'
        unique_together = [['event', 'position', 'student'], ['event', 'student']]


class EventBill(models.Model):
    STATUS = (
        ("unpaid", "unpaid"),
        ("partial payment", "partial payment"),
        ("paid", "paid")
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(default="unpaid", max_length=20, choices=STATUS)
    for_committee = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event}"

    class Meta:
        ordering = ['event']
        verbose_name = 'Event Bill'
        verbose_name_plural = 'Event Bills'
        db_table = 'event_bill'
        unique_together=["event", "student"]


class EventCollection(models.Model):
    METHOD = (
        ('Cash', 'Cash'),
        ('Mobile', 'Mobile'),
        ('Bank', 'Bank'),
    )
    event_bill = models.ForeignKey(EventBill, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method = models.CharField(max_length=10, choices=METHOD, default="Cash")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_bill)

    class Meta:
        ordering = ['event_bill']
        verbose_name = 'Event Collection'
        verbose_name_plural = 'Event Collections'
        db_table = 'event_collection'
