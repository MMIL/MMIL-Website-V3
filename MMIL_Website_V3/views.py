from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import contact_form
from django.core.mail import send_mail,EmailMultiAlternatives
from .settings import EMAIL_HOST_USER
from registration.models import Student_Registration
from contact.models import contactmsg
from django.utils import timezone


def index(request):
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
			interests=interests,
			branch=branch,
			year=year,
			email=email,
			phone_no=contact
			)
		register_data.save()
		return redirect('/')
	return render(request, "index/index.html",{})




def about(request):
	return render(request, "about/about.html",{})



def project(request):
	return render(request, "project/project.html",{})



def event(request):
	return render(request, "event/event.html",{})




def team(request):
	return render(request, "team/team.html",{})




def contact(request):
	form_class=contact_form(request.POST or None)
	content={
		"formu": form_class,
		"error":False,
		"Noerror":False,
	}
	if form_class.is_valid():
		print(form_class.cleaned_data)
		first_name=form_class.cleaned_data.get("first_name")
		last_name=form_class.cleaned_data.get("last_name")
		email=form_class.cleaned_data.get("email")
		subject=form_class.cleaned_data.get("subject")
		message=form_class.cleaned_data.get("message")
		try:
			newmsg=contactmsg.objects.create(
				firstname=first_name,
				lastname=last_name,
				email=email,
				subject=subject,
				message=message,
				subtime=timezone.now()
			)
		except:
			content["error"]=True
			return render(request,"contact/contact.html",content)
		newmsg.save()
		content["Noerror"]=True
		return render(request,"about/about.html",content)
		### For Sending Emails ##########################################################
		#################################################################################
		from_email=EMAIL_HOST_USER
		to_list=[EMAIL_HOST_USER,"shuklanushiv@gmail.com"]
		message="Hello Admin of MMIL \n \n A User wants to contact us with the following information as - \n\n Name -  "+first_name+" "+last_name+"\n E-mail - "+email+"\n Message - "+message
		### For Sending Emails ##########################################################
		#################################################################################
		send_mail(subject,message,from_email,to_list)
	return render(request, "contact/contact.html",content)



def gallery(request):
	return render(request, "gallery/gallery.html",{})



def zealicon(request):
	return render(request, "zealicon/zealicon.html",{})
