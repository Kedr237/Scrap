from django.http import HttpResponse


def base_view(request):
    return HttpResponse('<h1>Hello world!</h1>')
