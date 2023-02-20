from django.shortcuts import render, redirect
from .models import Room 
from .forms import ProjectForm
 # Create your views here.


# rooms = [
#     {'id':1 , 'name': 'Project 1'},
#     {'id':2 , 'name': 'Project 2'},
#     {'id':3 , 'name': 'Project 3'},
# ] 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}

    return render(request,'base/room.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def updateProject(request,pk):
    room = Room.objects.get(id=pk)
    form = ProjectForm(instance=room)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/project_form.html', context)


def deleteProject(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
