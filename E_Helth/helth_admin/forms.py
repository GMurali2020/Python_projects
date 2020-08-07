from django import forms
from .models import UserModel,MedicienandDiseasesModel
class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields="__all__"
class MedicienanddiseasesForm(forms.ModelForm):
    class Meta:
        model=MedicienandDiseasesModel
        fields="__all__"

from django.contrib.auth import authenticate,get_user_model
user=get_user_model()
class UserloginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        if username and password:
            user(password=password,username=username)
            if not user:
                raise forms.ValidationError("this user does not exist")
            if not user.check_password:
                raise forms.ValidationError("password incorrect")
            if not user.is_active:
                raise forms.ValidationError("user not active")
            return super(UserloginForm,self).clean(*args,**kwargs)
