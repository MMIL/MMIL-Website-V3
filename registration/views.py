from django.shortcuts import render
from .models import Student_Registration
from django.shortcuts import redirect
# Create your views here.



def registration(request):
	if request.POST:
		print(request.POST)
		name=request.POST.get('name')
		admission_no=request.POST.get('adm_no')
		department=request.POST.get('department')
		branch=request.POST.get('branch')
		year=request.POST.get('year')
		email=request.POST.get('email')
		contact=request.POST.get('contact')
		leng=len(department)
		print(type(department))
		interests=''
		for i in range(leng):
			interests=interests+department[i]+','
		register_data=Student_Registration(
			name=name,
			admission_no=admission_no,
			interests=department,
			branch=branch,
			year=year,
			email=email,
			phone_no=contact
			)
		register_data.save()
		return redirect('/')
	return render(request, "register/register.html",{})