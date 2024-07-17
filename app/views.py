from django.shortcuts import render

from .models import Person,Hello

def index_views(request):
    hellos = Hello.objects.all()

    return render(request,'app/index.html',{'hellos':hellos})
