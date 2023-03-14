from django.shortcuts import render

# Create your views here.
def operation_jinja(request):
    d={'a':190055,'b':190,'c':5201}
    return render(request,'operation_jinja.html',d)


def loops(request):
    d={'name':'farooq'}
    return render(request,'loops.html',d)