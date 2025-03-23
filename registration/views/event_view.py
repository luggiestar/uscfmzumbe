from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import EventForm, EventPaymentForm, EventCommitteeForm
from ..models import Event, Semester, EventBill, Student, EventCommittee, Committee, EventCollection


@login_required(login_url='/')
def events(request):
    template = 'registration/event.html'
    get_events = Event.objects.all()
    edit_event_forms = {depart.id: EventForm(instance=depart) for depart in get_events}

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = 'Event saved successfully'
                messages.success(request, message)
            except:
                message = f'Event name is unique'
                messages.error(request, message)
        else:
            message = 'Event not saved please make sure you enter valid data'
            messages.error(request, message)

        return redirect('events')

    context = {
        'events': get_events,
        'form': EventForm,
        'edit_event_forms': edit_event_forms
    }

    return render(request, template, context)


@login_required(login_url='/')
def update_event(request):
    if request.method == 'POST':
        try:
            event_id = request.POST.get('event_id')
            get_events = Event.objects.get(id=event_id)
            form = EventForm(request.POST, instance=get_events)
            if form.is_valid():
                form.save()
                message = f'Event updated successfully'
                messages.success(request, message)
            else:
                message = f'Somthing went wrong try again {form.errors}'
                messages.error(request, message)
        except:
            message = f'Something went wrong try again'
            messages.error(request, message)
    return redirect('events')


@login_required(login_url='/')
def event_committee(request, event_id):
    template = 'registration/event-committee.html'
    get_event = Event.objects.get(id=event_id)
    get_event_committee = EventCommittee.objects.filter(event_id=event_id)

    context = {
        'event_committees': get_event_committee,
        'get_event': get_event,
        'EventCommitteeForm': EventCommitteeForm
    }

    return render(request, template, context)


@login_required(login_url='/')
def save_event_committee(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        get_event = Event.objects.get(id=event_id)
        form = EventCommitteeForm(request.POST)
        if form.is_valid():
            try:
                get_form = form.save(commit=False)
                get_form.event = get_event
                get_form.save()
                message = 'Event saved successfully'
                messages.success(request, message)
            except Exception as e:
                message = f'Something went wrong try again {e}'
                messages.error(request, message)
        else:
            message = f'Something went wrong try again {form.errors}'
            messages.error(request, message)

        return redirect("event_committee", event_id)


@login_required(login_url='/')
def event_bills(request, event_id):
    template = 'registration/event-bills.html'
    get_event = Event.objects.get(id=event_id)
    get_event_bills = EventBill.objects.filter(event_id=event_id)

    context = {
        'event_bills': get_event_bills,
        'get_event': get_event,
        'EventPaymentForm': EventPaymentForm
    }

    return render(request, template, context)


@login_required(login_url='/')
def student_event_bills(request):
    template = 'registration/student-event-bills.html'
    get_event_bills = EventBill.objects.all()

    context = {
        'event_bills': get_event_bills,
        'EventPaymentForm': EventPaymentForm
    }

    return render(request, template, context)

@login_required(login_url='/')
def event_collection(request):
    template = 'registration/event-collection.html'
    get_event_collection = EventCollection.objects.all()

    context = {
        'event_collections': get_event_collection,
        'EventPaymentForm': EventPaymentForm
    }

    return render(request, template, context)


@login_required(login_url='/')
def generate_event_bill(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        get_event = Event.objects.get(id=event_id)
        get_student = Student.objects.exclude(status__in=["associate", "Associate"])
        get_event_committee = list(EventCommittee.objects.filter(event=get_event).values_list("student__id", flat=True))

        # generate bill for student of a specific events
        for student in get_student:
            try:
                if student.id in get_event_committee:
                    save_event_bill = EventBill(event=get_event, student=student, amount=get_event.committee_amount)
                else:
                    save_event_bill = EventBill(event=get_event, student=student, amount=get_event.member_amount)

                save_event_bill.save()
                messages.success(request, f"Bill generated successfully for {student.user.last_name}")
            except Exception as e:
                messages.error(request, f"Error processing row {student}: {e}")
                continue  # Skip to the next row if there's an error

        return redirect("event_bills", event_id)


@login_required(login_url='/')
def clear_event_bill(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        get_event = Event.objects.get(id=event_id)
        get_student = Student.objects.exclude(status__in=["associate", "Associate"])

        # clear bill for student of a specific events, on 0 paid payment bill wil be cleared
        for student in get_student:
            delete_event_bill = EventBill.objects.filter(student=student, event=get_event).first()
            if delete_event_bill.paid_amount > 0:
                pass
            else:
                delete_event_bill.delete()

        return redirect("event_bills", event_id)
