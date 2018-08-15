from django import forms




class contact_form(forms.Form):
	first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"input_field","placeholder":"Please Enter your First Name"}))
	last_name=forms.CharField( widget=forms.TextInput(attrs={"class":"input_field","placeholder":"Please Enter your Last Name"}))
	email=forms.CharField( widget=forms.TextInput(attrs={"class":"input_field","placeholder":"Please Enter your Email"}))
	subject=forms.CharField( widget=forms.TextInput(attrs={"class":"input_field","placeholder":"Please Enter the Subject"}))
	message=forms.CharField( widget=forms.Textarea(attrs={"class":"input_field","placeholder":"Message for us."}))