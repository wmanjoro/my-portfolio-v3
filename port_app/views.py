from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def testing_view(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())