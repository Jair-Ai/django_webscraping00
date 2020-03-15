from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(request):
    return render(request, template_name='base.html')

def new_search(request):
    search = request.POST.get('search')

    for_frontend = {'search': search}
    print(for_frontend)
    return render(request, template_name="new_search.html", context=search)