from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import TypeEquipment, Equipment
from .forms import NewEquipmentForm
from django.views.generic import ListView


# Create your views here.
def main(request):
    title = 'Добавить устройство'
    message = 'Серийный номер зарегестрирован'
    type_equipments = TypeEquipment.objects.all()
    if request.method == 'POST':
        equipment_form = NewEquipmentForm(data=request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            content = {'title': title}
            return render(request, 'mainapp/succes.html', content)
    else:
        equipment_form = NewEquipmentForm()
    content = {'title': title, 'equipment_form': equipment_form}
    return render(request, 'mainapp/main.html', content)


def succes(request):
    title = 'Устройство добавлено'
    content = {'title': title}
    return render(request, 'mainapp/succes.html', content)
