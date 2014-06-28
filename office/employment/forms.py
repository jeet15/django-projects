from django import forms
from models import Employer, Education

class EmployerForm(forms.Form):
	id = forms.CharField(required = False, widget = forms.HiddenInput())
	fname = forms.CharField(label = "First Name", max_length=20)
	mname = forms.CharField(label = "Middle Name", max_length=20 , required=False )
	lname = forms.CharField(label = "Last Name", max_length=20)
	city = forms.CharField(label = "City", max_length=50)
	state = forms.CharField(label = "State", max_length=50)
	country = forms.CharField(label = "Country", max_length=20)
	pincode = forms.CharField(label = "Pincode",max_length = 10)
	email = forms.CharField(label = "Email", max_length=40)
	mobile = forms.CharField(label = "Mobile Number", max_length=18)

	def save(self):
		data=self.cleaned_data
		#for udpate
		if data['id']:
			emp = Employer.objects.filter(id = data['id'])
			if emp:
				emp = emp[0]
				emp.fname = data['fname']
				emp.mname = data['mname']
				emp.lname = data['lname']
				emp.city = data['city']
				emp.state = data['state']
				emp.country = data['country']
				emp.pincode = data['pincode']
				emp.email = data['email']
				emp.mobile = data['mobile']
				emp.save()
		#For direct save
		emp = Employer(fname=data['fname'], mname=data['mname'], lname=data['lname'], city=data['city'], state=data['state'],
			country=data['country'], pincode=data['pincode'], email=data['email'], mobile=data['mobile'])
		emp.save()
		return True


class EducationForm(forms.Form):
	higher_specification = forms.CharField(label ="Higher Specification", max_length=20)
	higher_year = forms.CharField(label ="Passing Year", max_length = 10)
	secondary_specification = forms.CharField(label ="Secondary Specification", max_length=20)
	secondary_year = forms.CharField(label ="Passing Year",  max_length = 10)
	graduation = forms.CharField(label ="Graduation", max_length=20)
	year = forms.CharField(label ="Passing Year",  max_length = 10)
	university = forms.CharField(label ="University", max_length=50)

	def save(self):
		data=self.cleaned_data
		edu = Education(higher_specification = data['higher_specification'],
			higher_year = data['higher_year'] ,secondary_specification = data['secondary_specification'], 
			secondary_year = data['secondary_year'], graduation = data['graduation'],
			year = data['year'], university = data['university'])
		edu.save()
		return True