from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return redirect(reverse('index'))
	return render(request, 'app1/index.html')