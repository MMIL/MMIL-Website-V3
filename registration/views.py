from django.shortcuts import render

# Create your views here.



def registration(request):
	if request.POST:
		print("Arch")
	return render(request, "register/register.html",{})