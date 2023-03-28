from django.core.paginator import Paginator
from django.shortcuts import render
from home.models import Client

def client_list(request):
    client_list = Client.objects.all().order_by('nom')
    paginator = Paginator(client_list, 10)  # 10 clients par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'client_list.html', context)
