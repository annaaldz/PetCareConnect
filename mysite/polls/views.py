
# Create your viewimport requests
from django.shortcuts import render
from django.http import JsonResponse

def petCare_view(request):
    response = request.get('https://api-petcare.onrender.com/employees?auth=GciOiJIUzI1NiIsInR5cCI6I')
    data = response.json()
    return JsonResponse(data)
