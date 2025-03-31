from django.shortcuts import render
from .models import SustainabilityFactor

def certification_results(request):
    factors = SustainabilityFactor.objects.all()
    return render(request, 'certification/results.html', {'factors': factors})
