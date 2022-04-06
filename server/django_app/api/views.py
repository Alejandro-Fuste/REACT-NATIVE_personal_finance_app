from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create functions ------------------------------------------------------------
# Read functions ------------------------------------------------------------
# Update functions ------------------------------------------------------------
# Delete functions ------------------------------------------------------------


def say_hello(request):
    return HttpResponse("Hello World")


def sample_data(request):
    data = {
        'name': 'Victor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data, status=200)
