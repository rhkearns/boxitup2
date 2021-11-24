from django.db import models


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