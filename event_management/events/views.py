from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Location, Comment
from .forms import LocationForm
from .forms import EventForm, CommentForm
from django.contrib.auth.decorators import login_required


@login_required


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        else:
            print(form.errors)  # Вывод ошибок
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':    
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'events': event})


def event_detail(request, pk): 
    event = get_object_or_404(Event, pk=pk) 
    locations = event.locations.all()

    if request.method == 'POST': 
        if 'add_location' in request.POST:
            form = LocationForm(request.POST) 
            if form.is_valid(): 
                location = form.save(commit=False) 
                location.event = event
                location.save() 
                return redirect('event_detail', pk=event.pk) 
        elif 'edit_location' in request.POST: 
            location_id = request.POST.get('location_id') 
            location = get_object_or_404(Location, id=location_id)
            form = LocationForm(request.POST, instance=location) 
            if form.is_valid(): 
                form.save() 
                return redirect('event_detail', pk=event.pk) 
        elif 'delete_location' in request.POST: 
            location_id = request.POST.get('location_id') 
            location = get_object_or_404(Location, id=location_id) 
            location.delete() 
            return redirect('event_detail', pk=event.pk) 

    else: 
        form = LocationForm() 

    return render(request, 'events/event_detail.html', {
        'event': event,
        'locations': locations,
        'form': form,
    })


def location_comments(request, task_id):
    location = get_object_or_404(Location, id=task_id)
    comments = location.comments.all()

    if request.method == 'POST':
        if 'add_comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.locations = location
                comment.user = request.user
                comment.save()
                return redirect('location_comments', task_id=location.id)

        elif 'edit_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('location_comments', task_id=location.id)

        elif 'delete_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            comment.delete()
            return redirect('location_comments', task_id=location.id)

    else:
        form = CommentForm()

    return render(request, 'location_comments.html', {
        'location': location,
        'comments': comments,
        'form': form,
    })

