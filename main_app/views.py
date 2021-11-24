from django.shortcuts import render
from .models import Box

# Create your views here.
def home(request):
  return render(request, 'home.html')

def boxes_index(request):
  boxes = Box.objects.all()
  return render(request, 'boxes/index.html', {'boxes': boxes })