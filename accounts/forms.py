from django import forms
from django.forms import ModelForm
from accounts.models import TransferDetails
class AccountCreateForm(forms.Form):

    personname=forms.CharField(max_length=150)
    accno=forms.CharField(max_length=18)
    actype=forms.CharField(max_length=50)
    balance=forms.IntegerField()
    phonenumber=forms.CharField(max_length=12)
    mpin=forms.CharField(max_length=6)


class LoginForm(forms.Form):
    phonenumber=forms.CharField(max_length=15)
    mpin=forms.CharField(max_length=6)


class BalanceChkform(forms.Form):
    mpin = forms.CharField(max_length=6)

class TransferAmountForm(ModelForm):
    class Meta:
        model=TransferDetails
        fields=("mpin",)
