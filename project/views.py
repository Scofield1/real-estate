from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from myapp import settings
from .models import *
from email import message
from re import template
from django.core.mail import EmailMultiAlternatives
from django.template import loader


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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        template = loader.get_template('mail_form.txt')

        context = {'name': name, 'email': email,
                   'subject': subject, 'content': content}
        message = template.render(context)
        email = EmailMultiAlternatives(
            subject, message,
            'Easy Agency',
            [settings.EMAIL_HOST_USER, email])
        email.content_subtype = 'html'
        email.send()
        # messages.success(request, 'Message Sent Succesfully')
        return redirect('property', pk)
    context = {'data': data}
    return render(request, 'property-single.html', context)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        template = loader.get_template('mail_form.txt')

        context = {'name': name, 'email': email,
                   'subject': subject, 'content': content}
        message = template.render(context)
        email = EmailMultiAlternatives(
            subject, message,
            'Easy Agency',
            [settings.EMAIL_HOST_USER, email])
        email.content_subtype = 'html'
        email.send()
        messages.success(request, 'Message Sent Succesfully')
        return redirect('contact')
    return render(request, 'contact.html')
