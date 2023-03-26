from django.test import TestCase
from django.views.generic.edit import CreateView



# Create your tests here.



class Asset(CreateView):
    model = Asset;
    fields = 