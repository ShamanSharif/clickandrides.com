from django.shortcuts import render
from decouple import config

from .forms import BookForm

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
	else:
		form = BookForm()

	context = {
		'form': form,
	}
	return render(request, 'main/home.html', context)
