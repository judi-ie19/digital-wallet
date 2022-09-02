
from django.contrib import admin
from .models import Account, Card, Third_party
from .models import Customer
from .models import Wallet
from .models import Transaction
from .models import Notification
from .models import Third_party
from .models import Receipt
from .models import Loan
from .models import Reward



class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email')
    search_fields=("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
   list_display=('account_number','account_type','account_balance','account_name','wallet')
   search_fields=("account_number","account_type","account_balance","account_name","wallet")
admin.site.register(Account,AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("balance","customer","amount","time","status")
    search_fields=("balance","customer","amount","time","status")
admin.site.register(Wallet,WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_ref","transaction_amount","transaction_name","transaction_type","transaction_charge","date_and_time","receipt")
    search_fields=("transaction_ref","transaction_amount","transaction_name","transaction_type","transaction_charge","date_and_time","receipt")
admin.site.register(Transaction,TransactionAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("card_number","card_name","date_issued","card_type","expiry_date","security_code","account","issuer")
    search_fields=("card_number","card_name","date_issued","card_type","expiry_date","security_code","account","issuer")
admin.site.register(Card,CardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("name","transaction_Id","tittle","Receipt","status","date_and_time")
    search_fields=("name","transaction_Id","tittle","Receipt","status","date_and_time")
admin.site.register(Notification,NotificationAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("name","currency","account","type","location","amount")
    search_fields=("name","currency","account","type","location","amount")
admin.site.register(Third_party,Third_partyAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","date","bill_number","balance","amount","receipt_file")
    search_fields=("receipt_type","date","bill_number","balance","amount","receipt_file")
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("lookup_number","date_and_time","amount","loan_status","wallet","interest_rate","loan_term","payment_due_date","loan_balance","guarantor")
    search_fields=("lookup_number","date_and_time","amount","loan_status","wallet","interest_rate","loan_term","payment_due_date","loan_balance","guarantor")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("transaction","customer_Id","points","gender","third_party","date_time")
    search_fields=("transaction","customer_Id","points","gender","third_party","date_time")
admin.site.register(Reward,RewardAdmin)


# Register your models here.


