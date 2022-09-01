
from django import forms
from .models import Customer, Transaction,Wallet,Account

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields="__all__"
      
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields="__all__"

class AcountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields="__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields="__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields="__all__"




      