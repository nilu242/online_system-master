from allauth.account.forms import SignupForm


from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    mobile_number = forms.CharField(max_length=15, label='Mobile Number')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile_number = request.POST.get('mobile_number')
        user.save()
        return user
