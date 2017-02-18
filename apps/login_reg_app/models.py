from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from ..app1.models import Destination
import bcrypt, re

class UserManager(models.Manager):
    def validateReg(self, request):
        errors = self.validate_inputs(request)

        if len(errors) > 0:
            return (False, errors)
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], pw_hash=pw_hash)

        return (True, user)

    def validateLogin(self, request):
        try:
            user = User.objects.get(username=request.POST['username'])
            # The username matched a record in the database, now test passwords
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)

        except ObjectDoesNotExist:
            pass

        return (False, ["username/password don't match."])

    def validate_inputs(self, request):
        errors = []
        users = self.all()
        if request.POST['username'] in users:
            errors.append("username already exists!")
        if len(request.POST['first_name']) < 3 or len(request.POST['last_name']) < 3 or len(request.POST['username']) < 3:
            errors.append("Please include an input longer than three characters.")
        if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
            errors.append("Passwords must match and be at least 8 characters.")

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    trips = models.ManyToManyField(Destination, related_name = "users")
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)

    objects = UserManager()
