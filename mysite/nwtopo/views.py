from django.shortcuts import render

# Create your views here.
# Create your views here.
def nwtopo(request):
    return render(request, template_name='nwtopo.html')


def topo(request):
    return render(request, template_name='topo_nw.html')