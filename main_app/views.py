from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello World</h1>')

def boxes_index(request):
  return render(request, 'boxes/index.html', {'boxes': boxes })