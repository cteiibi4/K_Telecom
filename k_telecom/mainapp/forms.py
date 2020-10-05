from django.forms import ModelForm, ValidationError, CharField, ChoiceField
from django.http import HttpResponse, HttpRequest, QueryDict
import re
from .models import TypeEquipment, Equipment


class NewEquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ('serial_number', 'code_type')

    def __init__(self, *args, **kwargs):
        super(NewEquipmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        data = self.cleaned_data['serial_number']
        patter_obj = self.cleaned_data['code_type']
        obj = TypeEquipment.objects.get(name_type = patter_obj)
        pattern_base = getattr(obj, 'mask_serial_number')
        pattern_list = []
        print(pattern_base)
        for i in pattern_base:
            if i == 'Z':
                pattern_list.append(r'[-_@]')
            elif i == 'X':
                pattern_list.append(r'[A-Z0-9]')
            elif i == 'A':
                pattern_list.append(r'[A-Z]')
            elif i == 'a':
                pattern_list.append(r'[a-z]')
            elif i == 'N':
                pattern_list.append(r'[0-9]')
        pattern = ''.join(pattern_list)
        print(pattern)
        if re.search(pattern, data) is None:
            raise ValidationError('Неверный серийный номер')


