from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

def boxes_index(request):
  return render(request, 'boxes/index.html', {'boxes': boxes })