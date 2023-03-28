from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from apps.home.datatest import generate_code_client
# from apps.home.datatest_cotisation import generate_code_cotisation
from django.core.paginator import Paginator
from django.shortcuts import render
from apps.home.models import Client,Cotisation

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(f'home/{load_template}')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def client_list(request):
    client = Client.objects.all().order_by('-id')
    paginator = Paginator(client, 10)  # 10 clients par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'home/clients.html', context)

@login_required(login_url="/login/")
def client_info(request,pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'home/client_info.html', context)

@login_required(login_url="/login/")
def client_edit(request,pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'home/clients_edit.html', context)

@login_required(login_url="/login/")
def client_validate(request,pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'home/clients.html', context)

@login_required(login_url="/login/")
def cotisation_list(request):
    cotisation = Cotisation.objects.all().order_by('-id')
    paginator = Paginator(cotisation, 10)  # 10 clients par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'home/cotisations.html', context)

@login_required(login_url="/login/")
def cotisation_info(request,pk):
    client = Client.objects.get(id=pk)
    cotisation = Cotisation.objects.filter(code_client=client.code_client)
    context = {'client': client,'cotisation': cotisation}
    return render(request, 'home/cotisation_info.html', context)

