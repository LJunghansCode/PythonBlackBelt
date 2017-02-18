from __future__ import unicode_literals


from django.db import models



# Create your models here.


class DestinationManager(models.Manager):
	def new_destination(self, data):
		errors = []
		leaving = data['date_from']
		returning = data['date_to']
		print(returning)
		print(leaving)
		if leaving > returning:
			errors.append("Please come back AFTER you leave!")
		if not data['date_from'] or not data['date_to']:
			errors.append("Please enter a date!!")
		if not data["location"]:
			errors.append("Fields can not be blank")
		if not data["description"]:
			errors.append("Please enter a description!")

		response = {}

		if not errors:
			new_destination = self.create(name = data["location"], description=data['description'], datefrom=data["date_from"], dateto=data["date_to"], published = data["published"])
			response["added"] = True
			response["new_destination"] = new_destination
		else:
			response["added"] = False
			response["errors"] = errors

		return response	



class Destination(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=1000, null=True)
	published = models.CharField(max_length=55)
	datefrom = models.CharField(max_length=40)
	dateto = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = DestinationManager()