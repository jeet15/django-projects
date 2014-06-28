from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employment.models import Employer, Education
from forms import EmployerForm, EducationForm

def home(request):
	emp = Employer.objects.all()
	return render(request, 'employment/home.html' , {'emp':emp})

def add_employer(request):
	if 'POST' == request.method:
		form = EmployerForm(request.POST)
		edu = EducationForm(request.POST)
		if form.is_valid():
			if edu.is_valid():
				form.save()
				edu.save(id=id)
			messages.success(request, 'Details Inserted Successfully')
			return redirect('home')
		else:
			messages.error(request, 'submitted text is invalid')
	else:
		form = EmployerForm()
		edu = EducationForm()
	return render(request, 'employment/add.html', {'form':form,'edu':edu, 'action_title': 'Add Employer'})	

def view_employer(request, id):
	emp = Employer.objects.filter(id=id)
	if emp:
		emp = emp[0]
		return render (request, 'employment/view.html', {'emp':emp})
	else:
		messages.error(request, 'Selected Employer doesn,t exit')
		return redirect('home')

def edit_employer(request, id):
	emp = Employer.objects.filter(id = id)
	if emp:
		emp = emp[0]
		form = EmployerForm({
			'fname':emp.fname,
			'mname':emp.mname,
			'lname':emp.lname,
			'city':emp.city,
			'state':emp.state,
			'country':emp.country,
			'pincode':emp.pincode,
			'email':emp.email,
			'mobile':emp.mobile

			})
		return render(request, 'employment/add.html',{'form':form, 'action_title':'Update Employer Details'})
	else:
		messages.error(request, 'Selected Employer doesn,t exit')
		return redirect('home')
		



def add_education(request, id):
	emp = Employer.objects.all()
	if emp:
		emp = emp[0]
		if 'POST' == request.method:
			form = EducationForm(request.POST)
			if form.is_valid():
				form.save()
		else:
			form = EducationForm()
		return render(request, 'employment/more.html', {'form':form, 'action_title': 'Add Education', 'emp':emp})	
					
	
def del_profile(request, id):
	remove = Employer.objects.filter(id=id)
	if remove:
		remove.delete()
		messages.success(request, 'Profile deleted Successfully......')
	else:
		messages.error(request,'Selected profile doesn,t exit')
	return redirect('home')	
def confirm_delete(request,id):
	remove = Employer.objects.filter(id=id)
	if remove:
		remove = remove[0]
	return render(request,'employment/delete.html', {'remove':remove})	


# Create your views here.
