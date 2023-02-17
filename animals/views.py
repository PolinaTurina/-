from django.shortcuts import render
from .models import Animal


def animal_detail_view(request, animal_pk):
    animal = Animal.objects.get(pk=animal_pk)
    context = {"animal": animal}
    return render(request, "animals/animal_detail.html", context)


def animal_list_view(request):
    animals = Animal.objects.all()
    context = {"animal_list": animals}
    return render(request, "animals/animal_list.html", context)
