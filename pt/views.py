from django.shortcuts import render

def landing(request):

    c = {}

    return render(request, 'periodic-table.html', c)
