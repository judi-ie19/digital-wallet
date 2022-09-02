
from django import forms
from .models import Customer, Notification, Transaction,Wallet,Account,Card,Third_party,Notification,Receipt,Loan,Reward

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer      
        fields="__all__"
      
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields="__all__"

class Acount_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields="__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields="__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields="__all__"

class ThirdpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Third_party
        fields="__all__"


class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields="__all__"


class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields="__all__"

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields="__all__"

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields="__all__"

      