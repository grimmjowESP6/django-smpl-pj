from django.shortcuts import render,redirect
from webapp.forms import ContactForm
# Create your views here.
def index(request):
    cont = ContactForm()
    return render(request, 'index.html',{'cform':cont})