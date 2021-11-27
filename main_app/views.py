from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Box, Item
from .forms import ItemForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

@login_required
def boxes_index(request):
  boxes = Box.objects.filter(user=request.user)
  return render(request, 'boxes/index.html', {'boxes': boxes })

@login_required
def boxes_detail(request, box_id):
  box = Box.objects.get(id=box_id)
  item_form = ItemForm()
  return render(request, 'boxes/detail.html', {'box': box, 'item_form': item_form })

class BoxCreate(LoginRequiredMixin, CreateView):
  model = Box
  fields = ['number', 'size', 'category']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BoxUpdate(LoginRequiredMixin, UpdateView):
  model = Box
  fields = ['size', 'category']

class BoxDelete(LoginRequiredMixin, DeleteView):
  model = Box
  success_url = '/boxes/'

def add_item(request, box_id):
  form = ItemForm(request.POST)
  if form.is_valid():
    new_item = form.save(commit=False)
    new_item.box_id = box_id
    new_item.save()
  return redirect('boxes_detail', box_id=box_id)

def delete_item(request, box_id, item_id):
  Item.objects.get(id=item_id).delete()
  return redirect('boxes_detail', box_id=box_id)

def close_box(request, box_id):
  box = Box.objects.get(id=box_id)
  if box.isClosed:
    setattr(box, 'isClosed', False)
  else:
    setattr(box, 'isClosed', True)
  box.save()
  return redirect('boxes_detail', box_id=box_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('boxes_index')
    else:
      error_message = 'Invalid sign up -- please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)