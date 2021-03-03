from django.shortcuts import render, HttpResponse, redirect
from .models import Shows
from django.contrib import messages
from datetime import date
def shows(request):
     # GET THE SHOWS TO UPLOAD TO THE GRID
    shows_to_grid = Shows.objects.all()
    context = {'shows' : shows_to_grid}
    return render(request, "shows.html", context)

def show_form(request):
    return render(request, "new.html")
    
def add_show(request):
    print(request.POST['n_title'])
    if request.POST:
        add_show = Shows.objects.create(title=request.POST['n_title'],
                                        network=request.POST['n_network'], 
                                        release_date=date.today(), 
                                        description=request.POST['n_description'])
    return redirect('/shows')




def edit(request):
    return render(request, "edit.html")

def description(request):
    return render(request, "description.html")


