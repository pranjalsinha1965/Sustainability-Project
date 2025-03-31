from django.shortcuts import render
from .models import Cooperative, Bank, ITI, DISCOM

def building_list(request):
    cooperatives = Cooperative.objects.all()
    banks = Bank.objects.all()
    itis = ITI.objects.all()
    discoms = DISCOM.objects.all()
    
    context = {
        'cooperatives': cooperatives,
        'banks': banks,
        'itis': itis,
        'discoms': discoms
    }
    
    return render(request, 'building/list.html', context)
