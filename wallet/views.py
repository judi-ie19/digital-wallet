from django.shortcuts import render

from wallet.models import Wallet
from .forms import CustomerRegistrationForm,WalletRegistrationForm,AcountRegistrationForm,TransactionRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,'wallet/register_customer.html',{"form":form})
 
def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,'wallet/register_wallet.html',{"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,'wallet/register_account.html',{"form":form})
 
def register_transaction(request):
    form =TransactionRegistrationForm()
    return render(request,'wallet/register_transaction.html',{"form":form})
 