
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    # authentication paths
    path('', login_view, name="login"),
    path('user-logout', logout_view, name="logout"),
    path('change-password', change_password_view, name='change_password'),

    # dashboards
    path('dashboard', dashboard, name='dashboard'),

    # academic urls
    # academic
    path('unit', unit, name="unit"),
    path('update-unit', update_unit, name="update_unit"),
    path('delete-unit', delete_unit, name="delete_unit"),

    path('department', department, name="department"),
    path('update_department', update_department, name="update_department"),
    path('delete_department', delete_department, name="delete_department"),

    path('programme', programme, name="programme"),
    path('update_programme', update_programme, name="update_programme"),
    path('delete_programme', delete_programme, name="delete_programme"),

    path('year', year, name="year"),
    path('update-year', update_year, name="update_year"),
    path('delete-year', delete_year, name="delete_year"),

    # semester
    path('semester', semester, name="semester"),
    path('update_semester', update_semester, name="update_semester"),
    path('delete_semester', delete_semester, name="delete_semester"),
    path('set-semester-to-current', set_semester_to_current, name="set_semester_to_current"),

    # users
    path('users', users, name='users'),
    path('update-user', update_user, name='update_user'),
    path('delete-user', delete_user, name='delete_user'),

    # students
    path('students', students, name='students'),
    path('student-self-registration', self_student_registration, name='self_student_registration'),
    path('upload_student', upload_student, name='upload_student'),
    path('filter-member/<status>', filter_member, name='filter_member'),
    path('delete-student', delete_student, name='delete_student'),
    path('save-student', save_student, name='save_student'),
    path('send-sms-to-students', send_sms_to_students, name='send_sms_to_students'),
    path('student-committee', student_committee, name='student_committee'),
    path('committee', committee, name='committee'),
    path('update_committee', update_committee, name='update_committee'),

    path('position-list', position, name="positions"),
    path('change-position', update_position, name="update_position"),
    path('delete-position', delete_position, name="delete_position"),


    # payments
    path('bills-list', bills, name="bills"),
    path('generate-bill', generate_bill, name="generate_bill"),
    path('accounts-list', accounts, name="accounts"),
    path('student-bills-list', student_bills, name="student_bills"),
    path('save-payment', save_payment, name="save_payment"),
    path('stduent-bill-payments-list', student_bill_payments, name="student_bill_payments"),

    # events
    path('events', events, name="events"),
    path('student-event-bills', student_event_bills, name="student_event_bills"),
    path('student-collection', event_collection, name="event_collection"),
    path('event-committee/<event_id>', event_committee, name="event_committee"),
    path('save-event-committee', save_event_committee, name="save_event_committee"),
    path('generate-event-bill', generate_event_bill, name="generate_event_bill"),
    path('clear-event-bill', clear_event_bill, name="clear_event_bill"),
    path('event-bill/<event_id>', event_bills, name="event_bills"),
    path('update_event', update_event, name="update_event"),

]
