from django.db import models
from django.urls import reverse

SIZES = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large'),
  ('XL', 'Extra-Large')
)

# Create your models here.
class Box(models.Model):
  number = models.IntegerField()
  size = models.TextField(
    max_length=2,
    choices=SIZES,
    default=SIZES[1][0]
  )
  category = models.CharField(max_length=20)
  isClosed = models.BooleanField(default=False)

  def __str__(self):
    return str(self.number)

  def get_absolute_url(self):
    return reverse('boxes_detail', kwargs={'box_id': self.id })

class Item(models.Model):
  name = models.CharField(max_length=30)
  quantity = models.IntegerField()
  box = models.ForeignKey(Box, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name}: {self.quantity}"