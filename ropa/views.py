from django.shortcuts import render

# Create your views here.
def ropa_list(request):
    return render(request, 'ropa/ropa_list.html',{})