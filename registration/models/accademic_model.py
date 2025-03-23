from django.core.exceptions import ValidationError
from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abb = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abb

    class Meta:
        db_table = "unit"
        unique_together = ['name', 'abb']

    def save(self, *args, **kwargs):
        if self.name:
            self.name = str(self.name).lower()

        super(Unit, self).save(*args, **kwargs)


class Level(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Level"

    def save(self, *args, **kwargs):
        if self.name:
            self.name = str(self.name).lower()

        super(Level, self).save(*args, **kwargs)


class Year(models.Model):
    name = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    NAME = (
        ('semester 1', 'semester 1'),
        ('semester 2', 'semester 2'),
    )
    name = models.CharField(max_length=40, choices=NAME)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.year}'

    class Meta:
        db_table = "semester"

    def save(self, *args, **kwargs):
        # Check if is_current is set to True
        if self.is_current:
            # Look for an existing semester with is_current=True
            existing_current = Semester.objects.filter(is_current=True).exclude(pk=self.pk).exists()
            if existing_current:
                raise ValidationError("Only one semester can be set as current.")

        # Save the semester
        super().save(*args, **kwargs)


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abb = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, related_name='dept_uni')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abb

    class Meta:
        db_table = "department"
        unique_together = ['name', 'abb']

    def save(self, *args, **kwargs):
        if self.name:
            self.name = str(self.name).lower()

        super(Department, self).save(*args, **kwargs)


class Programme(models.Model):
    DURATION = (
        ('1', 'One Year'),
        ('2', 'Two Years'),
        ('3', 'Three Years'),
        ('4', 'Four Years'),
        ('5', 'Five Years'),
    )
    name = models.CharField(max_length=150, unique=True)
    abb = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, related_name='dept_prog')
    level = models.ForeignKey(Level, on_delete=models.RESTRICT, related_name='prog_level')
    duration = models.PositiveIntegerField(choices=DURATION)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abb

    class Meta:
        db_table = "programme"
        unique_together = [
            ['name', 'abb'],
            ['name', 'abb', 'department'],
            ['duration', 'name', 'abb']
        ]

    def save(self, *args, **kwargs):
        if self.name:
            self.name = str(self.name).lower()

        super(Programme, self).save(*args, **kwargs)
