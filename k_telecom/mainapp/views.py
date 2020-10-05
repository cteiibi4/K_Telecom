from django.shortcuts import render, get_object_or_404
from .models import TypeEquipment, Equipment
from  .forms import NewEquipmentForm
from django.views.generic import ListView

# Create your views here.
def main(request):
    title = 'Добавить устройство'
    type_equipments = TypeEquipment.objects.all()

    if request.method == 'POST':
        equipment_form = NewEquipmentForm(data=request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            return render(request, 'mainapp/main.html')
    else:
        equipment_form = NewEquipmentForm()
    content = {'title': title, 'equipment_form': equipment_form}
    return render(request, 'mainapp/main.html', content)
