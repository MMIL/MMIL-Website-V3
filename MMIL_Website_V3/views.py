from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import contact_form
from django.core.mail import send_mail,EmailMultiAlternatives
from .settings import EMAIL_HOST_USER


def index(request):
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
		"formu": form_class
	}
	if form_class.is_valid():
		print(form_class.cleaned_data)
		first_name=form_class.cleaned_data.get("first_name")
		last_name=form_class.cleaned_data.get("last_name")
		email=form_class.cleaned_data.get("email")
		subject=form_class.cleaned_data.get("subject")
		message=form_class.cleaned_data.get("message")
		### For Sending Emails ##########################################################
		#################################################################################
		from_email=EMAIL_HOST_USER
		to_list=[EMAIL_HOST_USER,"dwevediar@gmail.com"]
		message="Hello Admin of MMIL \n \n A User wants to contact us with the following information as - \n\n Name -  "+first_name+" "+last_name+"\n E-mail - "+email+"\n Message - "+message
		### For Sending Emails ##########################################################
		#################################################################################
		send_mail(subject,message,from_email,to_list)
	return render(request, "contact/contact.html",content)



def gallery(request):
	return render(request, "gallery/gallery.html",{})



def zealicon(request):
	return render(request, "zealicon/zealicon.html",{})
