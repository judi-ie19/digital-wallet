
from django.utils import timezone
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Wallet(models.Model):
    balance=models.IntegerField()
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='wallet_customer')
    amount=models.IntegerField()
    time=models.DateTimeField(default=timezone.now)
    # currency=models.ForeignKey('currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    status=models.CharField(max_length=20)


class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=20)
    account_balance=models.IntegerField()
    account_name=models.CharField(max_length=20)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet',null=True)
   
class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=20)
    # Wallet=models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_name=models.CharField(max_length=20)
    transaction_type=models.CharField(max_length=20)
    transaction_charge=models.IntegerField()
    date_and_time=models.DateTimeField(null=True)
    receipt=models.CharField(max_length=20)
   
class Card(models.Model):
    card_number=models.IntegerField()
    card_name=models.CharField(max_length=20)
    date_issued=models.DateTimeField(null=True)
    card_type=models.CharField(max_length=20)
    expiry_date=models.IntegerField()
    security_code=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer=models.CharField(max_length=20)
   
class Third_party(models.Model):
    name=models.CharField(max_length=20)
    currency=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Third_party_currency',null=True)
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Third_party_account',null=True)
    type=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    amount=models.IntegerField()
 
   
class Notification(models.Model):
    name=models.CharField(max_length=20)
    transaction_Id=models.CharField(max_length=20)
    tittle=models.CharField(max_length=20)
    Receipt=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Notification_receipt',null=True)
    status=models.CharField(max_length=20)
    date_and_time=models.DateTimeField(null=True)
   
class Receipt(models.Model):
    receipt_type=models.CharField(max_length=20)
    date=models.DateField()
    bill_number=models.CharField(max_length=20)
    balance=models.IntegerField()
    amount=models.IntegerField()
    # transaction=models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Receipt_transaction',null=True)
    receipt_file=models.FileField
class Loan(models.Model):
    lookup_number=models.IntegerField()
    date_and_time=models.DateTimeField(null=True)
    amount=models.IntegerField()
    loan_status=models.CharField(max_length=20)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate=models.IntegerField()
    loan_term=models.CharField
    payment_due_date=models.IntegerField()
    loan_balance=models.IntegerField()
    guarantor=models.CharField(max_length=20)


class Reward(models.Model):
    transaction=models.CharField(max_length=20)
    customer_Id=models.IntegerField()
    points=models.IntegerField()
    gender=models.CharField(max_length=20)
    third_party=models.ForeignKey('Third_party',on_delete=models.CASCADE,related_name='Reward_third_party',null=True)
    date_time=models.DateTimeField(null=True) 

# class Currency(models.Model):
#     origin=models.CharField(max_length=15)
#     Symbol=models.CharField(max_length=15)
#     amount=models.IntegerField()

