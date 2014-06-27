from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
	fname = models.CharField("First Name", max_length=20)
	mname = models.CharField("Middle Name", max_length=20 )
	lname = models.CharField("Last Name", max_length=20)
	city = models.CharField("City", max_length=50)
	state = models.CharField("State", max_length=50)
	country = models.CharField("Country", max_length=20)
	pincode = models.CharField("Pincode", max_length = 10)
	email = models.CharField("Email", max_length=40)
	mobile = models.CharField("Mobile Number", max_length =18)


class Education(models.Model):
	employer = models.ForeignKey(Employer)
	higher_specification = models.CharField("Specification", max_length=20)
	higher_year = models.CharField("Passing Year", max_length = 10)
	secondary_specification = models.CharField("Specification", max_length=20)
	secondary_year = models.CharField("Passing Year", max_length = 10)
	graduation = models.CharField("Graduation", max_length=20)
	year = models.CharField("Passing Year", max_length = 10 )
	university = models.CharField("University", max_length=50)


# Create your models here.
