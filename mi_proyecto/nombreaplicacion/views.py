from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("Mensaje de la vista 1")

def vista_dos(request):
    return HttpResponse("Mensaje de la vista 2")

def vista_tres(request):
    return HttpResponse("Mensaje de la vista 3")
