from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Box

# Create your views here.
def home(request):
  return render(request, 'home.html')

def boxes_index(request):
  boxes = Box.objects.all()
  return render(request, 'boxes/index.html', {'boxes': boxes })

def boxes_detail(request, box_id):
  box = Box.objects.get(id=box_id)
  return render(request, 'boxes/detail.html', {'box': box })

class BoxCreate(CreateView):
  model = Box
  fields = ['number', 'size', 'category']

class BoxUpdate(UpdateView):
  model = Box
  fields = ['size', 'category']

class BoxDelete(DeleteView):
  model = Box
  success_url = '/boxes/'
