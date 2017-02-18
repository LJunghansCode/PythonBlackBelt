from django.shortcuts import render, redirect, reverse
from models import Destination
from ..login_reg_app.models import User
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user' not in request.session:		
		return redirect(reverse('index'))
	context = {
		"me" : Destination.objects.filter(users = request.session['user']['id']),

		"everyone": Destination.objects.exclude(published = request.session['user']['username'])
	} 
	return render(request, 'app1/index.html', context)
################### show new page #################################
def add_trip(request):
	return render(request, 'app1/add.html')
################## Join user to trip didnt want to make manager for it ###############
def join_trip(request): 
	user = User.objects.get(id = request.POST['user_id'])
	destination = Destination.objects.get(id = request.POST["destination_id"])
	user.trips.add(destination)
	messages.success(request, 'Yeah you are going now!')
	return redirect(reverse('travels'))	
	
################### specific destinations #########################
def show_destinations(request, dest_id):
	me = request.session['user']['id']
	destination =  Destination.objects.get(id = dest_id)
	context = {
		'destination': destination,
		'travellers': destination.users.exclude(id = me)
	}
	return render(request, 'app1/destination.html', context)
################### creating dest #################################
def create_destination(request):
	response = Destination.objects.new_destination(request.POST) 
	if response["added"]:
		user = User.objects.get(id = request.session['user']['id'])
		destination = Destination.objects.get(id = response["new_destination"].id)
		user.trips.add(destination)
		messages.success(request, 'added destination')
	else:
		for error in response['errors']:
			messages.error(request, error)
			return redirect(reverse('add_trip'))
	return redirect(reverse('travels'))
#################### messages ################################

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)
