from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Box
from .forms import ItemForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def boxes_index(request):
  boxes = Box.objects.all()
  return render(request, 'boxes/index.html', {'boxes': boxes })

def boxes_detail(request, box_id):
  box = Box.objects.get(id=box_id)
  item_form = ItemForm()
  return render(request, 'boxes/detail.html', {'box': box, 'item_form': item_form })

class BoxCreate(CreateView):
  model = Box
  fields = ['number', 'size', 'category']

class BoxUpdate(UpdateView):
  model = Box
  fields = ['size', 'category']

class BoxDelete(DeleteView):
  model = Box
  success_url = '/boxes/'

def add_item(request, box_id):
  form = ItemForm(request.POST)
  if form.is_valid():
    new_item = form.save(commit=False)
    new_item.box_id = box_id
    new_item.save()
  return redirect('boxes_detail', box_id=box_id)