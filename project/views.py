from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def index(request):
    agents = Agent.objects.all()
    context = {'agents': agents}
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about.html')


def agents_page(request):
    # setup pagination
    agents = Agent.objects.all().order_by('id')
    page = Paginator(agents, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {'page': page}
    return render(request, 'agents-grid.html', context)


def property_page(request):
    # setup pagination
    property_list = Property.objects.all()
    page = Paginator(property_list, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {'page': page}
    return render(request, 'property-grid.html', context)


def single_property(request, pk):
    data = Property.objects.get(pk=pk)
    context = {'data': data}
    return render(request, 'property-single.html', context)