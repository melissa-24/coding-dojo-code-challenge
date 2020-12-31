from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shows

def shows(request):
    context = {
        "shows" : Shows.objects.all()
    }
    return render(request, "tv_show_app/shows.html", context)

def new(request):
    return render(request, "tv_show_app/new.html")

def display_show(request, show_id):
    context={
        "show": Shows.objects.get(id=show_id),
    }
    return render (request, "tv_show_app/display_show.html", context)

def add_show(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect("/shows/new")
    new_show = Shows.objects.create(
        title=request.POST["title"],
        network=request.POST["network"],
        release_date=request.POST["release_date"],
        decription=request.POST["decription"],
        )
    return redirect("/shows/" + str(new_show.id))

def edit_page(request, show_id):
    context = {
        "show": Shows.objects.get(id=show_id),
    }
    return render (request, "tv_show_app/edit.html", context)

def edit_show(request, show_id):
    edit_show = Shows.objects.get(id=show_id)
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect(f"/shows/{edit_show.id}/edit/")
    edit_show.title = request.POST["title"]
    edit_show.network = request.POST["network"]
    edit_show.release_date = request.POST["release_date"]
    edit_show.decription = request.POST["decription"]
    edit_show.save()
    return redirect ("/shows/" + str(edit_show.id))



def destroy(request, show_id):
    Shows.objects.get(id = show_id).delete()
    return redirect ("/shows")
