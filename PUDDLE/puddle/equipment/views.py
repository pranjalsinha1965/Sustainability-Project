from django.shortcuts import render
from .models import Equipment

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment': equipment})
