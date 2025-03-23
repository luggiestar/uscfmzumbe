from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.site_header = 'USCF'
admin.site.site_title = 'USCF'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'username', 'email', 'first_name', 'middle_name', 'last_name', 'phone', 'sex',
        'is_active',
        'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('personal', {'fields': ('first_name', 'middle_name', 'last_name', 'sex', 'phone'),
                      }),

        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups',
                                    'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'middle_name', 'last_name', 'phone', 'sex', 'username',
                'password1',
                'password2',)}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'abb', 'created', 'updated']
    list_filter = ['abb', 'created', 'updated']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'abb', 'unit', 'created', 'updated']
    list_filter = ['abb', 'unit', 'created', 'updated']


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'semester', 'created', 'updated']
    list_filter = ['name', 'amount', 'semester', 'created', 'updated']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance', 'created', 'updated']
    list_filter = ['name', 'balance', 'created', 'updated']


@admin.register(StudentBill)
class StudentBillAdmin(admin.ModelAdmin):
    list_display = ['student', 'bill', 'paid_amount', 'status', 'created', 'updated']
    list_filter = ['student', 'bill', 'paid_amount', 'created', 'updated']


@admin.register(StudentBillPayment)
class StudentBillPaymentAdmin(admin.ModelAdmin):
    list_display = ['student_bill', 'amount', 'created', 'updated']
    list_filter = ['student_bill', 'amount', 'created', 'updated']


@admin.register(EventBill)
class EventBillAdmin(admin.ModelAdmin):
    list_display = ['event', 'student', 'amount', 'paid_amount', 'created', 'updated']
    list_filter = ['event', 'amount', 'created', 'updated']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated']
    list_filter = ['created', 'updated']


@admin.register(EventCommittee)
class EventCommitteeAdmin(admin.ModelAdmin):
    list_display = ['event', 'student', 'position', 'created', 'updated']
    list_filter = ['event', 'created', 'updated']


@admin.register(EventCollection)
class EventCollectionAdmin(admin.ModelAdmin):
    list_display = ['event_bill', 'paid_amount', 'method', 'created', 'updated']
    list_filter = ['created', 'updated']


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'is_current', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['name', 'abb', 'level', 'department', 'created', 'updated']
    list_filter = ['abb', 'department', 'level', 'created', 'updated']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_first_name', 'student_last_name', 'programme_abb', 'programme_level', 'year_of_study',
                    'created', 'updated']
    list_filter = ['user', 'created', 'updated']
    search_fields = ['user', ]

    def student_first_name(self, obj):
        return obj.user.first_name

    def student_last_name(self, obj):
        return obj.user.last_name

    def programme_abb(self, obj):
        return obj.programme.abb

    def programme_level(self, obj):
        return obj.programme.abb

    student_first_name.short_description = "First Name"
    student_last_name.short_description = "Last Name"
    programme_abb.short_description = "Programme"
    programme_level.short_description = "Level"


@admin.register(StudentCommittee)
class StudentCommitteeAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'committee_name', 'is_active', 'updated', 'created',)
    list_filter = ('committee',)
    search_fields = ('committee', 'user')
    ordering = ('created',)

    def user_first_name(self, obj):
        return obj.student.user.first_name

    def user_last_name(self, obj):
        return obj.student.user.last_name

    def committee_name(self, obj):
        return obj.committee.abb

    user_first_name.short_description = "First Name"
    user_last_name.short_description = "Last Name"
    committee_name.short_description = "Committee"
