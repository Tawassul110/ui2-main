from django.shortcuts import render
from apps.algorithms.views import get_option

# Create your views here.
def index(request):
    context = {
        'option' : get_option()
    }
    return render(request, 'pages/index.html', context)
