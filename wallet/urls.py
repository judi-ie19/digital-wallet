from django.urls import path

from .views import  list_Customers, list_card, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, register_account ,register_customer, register_notification, register_reward, register_transaction,register_wallet,register_account,register_card,register_thirdparty,register_receipt,register_loan
from .views import list_wallet,list_account
urlpatterns=[
    path("register/",register_customer,name="registation"),
    path("registerwallet/",register_wallet,name="registation"),
    path("registeraccount/",register_account,name="registation"),
    path("registertransaction/",register_transaction,name="registation"),
    path("registercard/",register_card,name="registation"),
    path("registerthird_party/",register_thirdparty,name="registation"),
    path("registernotification/",register_notification,name="registation"),
    path("registerreceipt/",register_receipt,name="registation"),
    path("registerloan/",register_loan,name="registation"),
    path("registerreward/",register_reward,name="registation"),
    path("customers/",list_Customers,name="customers-list"),
    path("wallets/", list_wallet,name="wallets-list"),
    path("accounts/", list_account,name="accounts-list"),
    path("loans/", list_loan,name="loans-list"),
    path("transactions/", list_transaction,name="transactions-list"),
    path("cards/", list_card,name="cards-list"),
    path("notifications/", list_notification,name="notifications-list"),
    path("thirdpartys/", list_thirdparty,name="thirdpartys-list"),
    path("rewards/", list_reward,name="rewards-list"),
    path("receipts/", list_receipt,name="receipts-list"),












    
]