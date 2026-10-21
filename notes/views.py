from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Django Notes App - CI/CD Working!</h1>")
