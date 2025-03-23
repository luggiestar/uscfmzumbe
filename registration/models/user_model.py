from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from ..validators import phone_regex
from .accademic_model import Programme


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError('The Username must be set')
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=100, null=True, blank=False)
    middle_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(choices=GENDER, max_length=1, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, null=True, blank=True)
    profile = models.ImageField(upload_to='profile')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Student(models.Model):
    STATUS = (
        ('continuing', 'Continuing'),
        ('finalist', 'finalist'),
        ('associate', 'associate'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_programme')
    programme = models.ForeignKey(Programme, on_delete=models.RESTRICT, related_name='student_prog')
    year_of_study = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS, max_length=12, default='continuing')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}-{self.programme}'

    class Meta:
        db_table = 'student'
        unique_together = ['programme', 'user']

    def save(self, *args, **kwargs):
        if self.year_of_study == self.programme.duration:
            self.status = 'finalist'

        if self.year_of_study < self.programme.duration:
            self.status = 'continuing'

        if self.year_of_study > self.programme.duration:
            self.status = 'associate'

        super().save(*args, **kwargs)


class Committee(models.Model):
    name = models.CharField(max_length=150, unique=True)
    abb = models.CharField(max_length=15, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'committee'
        unique_together = ['name', 'abb']


class StudentCommittee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_committee')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='committee_member')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student}-{self.committee}'

    class Meta:
        db_table = 'student_committee'
        unique_together = ['student', 'committee']


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'position'
