from django.shortcuts import render




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def curriculum(request):
    return render(request, 'curriculum.html')
def admission(request):
    return render(request, 'admission.html')
def contact(request):
    return render(request, 'contact.html')
def facility(request):
    return render(request, 'facility.html')
def gallery(request):
    return render(request, 'gallery.html')
