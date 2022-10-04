from django.shortcuts import render
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Transaction,Wallet,Third_party


from wallet.models import Third_party, Wallet,Transaction,Notification,Loan,Receipt,Customer,Card,Account
from .forms import CustomerRegistrationForm,WalletRegistrationForm,Acount_RegistrationForm,TransactionRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,NotificationRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm

# Create your views here.
def  list_Customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{
        "Watu":customers
    })
def register_customer(request):
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm

    return render(request,'wallet/register_customer.html',{"form":form})


def list_wallet(request):
    Wallets=Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',{"Wallets":Wallets})

def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm

    return render(request,'wallet/register_wallet.html',{"form":form})


def list_account(request):
    Accounts = Account.objects.all()
    return render(request,'wallet/accounts_list.html',{"Accounts":Accounts})

def register_account(request):
    if request.method=="POST":
        form=Acount_RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Acount_RegistrationForm

    return render(request,'wallet/register_account.html',{"form":form})

 
def list_transaction(request):
    Transactions=Transaction.objects.all()
    return render(request,'wallet/transactions_list.html',{"Transactions":Transactions})

def register_transaction(request):
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm

    return render(request,'wallet/register_transaction.html',{"form":form})


def list_card(request):
    Cards =Card.objects.all()
    return render(request,'wallet/cards_list.html',{"Cards":Cards})

def register_card(request):
    if request.method=="POST":
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm

    return render(request,'wallet/register_card.html',{"form":form})


def list_thirdparty(request):
    third_partys =Third_party.objects.all()
    return render(request,'wallet/thirdpartys_list.html',{"third_partys":third_partys})

def register_thirdparty(request):
    if request.method=="POST":
        form=ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdpartyRegistrationForm

    return render(request,'wallet/register_thirdparty.html',{"form":form})


def list_notification(request):
    Notifications= Notification.objects.all()
    return render(request,'wallet/notifications_list.html',{"Notifications":Notifications})

def register_notification(request):
    if request.method=="POST":
        form=NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm

    return render(request,'wallet/register_notification.html',{"form":form})



def list_receipt(request):
    Receipts =Receipt.objects.all()
    return render(request,'wallet/receipts_list.html',{"form":Receipts})

def register_receipt(request):
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm

    return render(request,'wallet/register_receipt.html',{"form":form})



def list_loan(request):
    Loans=Loan.objects.all()
    return render(request,'wallet/loan_list.html',{"Loans":Loans})

def register_loan(request):
    if request.method=="POST":
        form=LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm

    return render(request,'wallet/register_loan.html',{"form":form})


def list_reward(request):
    rewards =Reward.objects.all()
    return render(request,'wallet/rewards_list.html',{"rewards":rewards})

def register_reward(request):
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm

    return render(request,'wallet/register_reward.html',{"form":form})



        
        






    


 