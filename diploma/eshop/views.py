from django.shortcuts import render

def main_page(request):
    template = 'index.html'
    return render(request, template)

def show_phone(request):
    template = 'phone.html'
    return render(request, template)
