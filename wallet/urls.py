from django.urls import path
from .views import register_account ,register_customer, register_notification, register_reward, register_transaction,register_wallet,register_account,register_card,register_thirdparty,register_receipt,register_loan
 

urlpatterns=[
    path("register/",register_customer,name="registation"),
    path("registerwallet/",register_wallet,name="registation"),
    path("registeraccount/",register_account,name="registation"),
    path("registertransaction/",register_transaction,name="registation"),
    path("registercard/",register_card,name="registation"),
    path("registerthird_party/",register_thirdparty,name="registation"),
    path("registernotification_/",register_notification,name="registation"),
    path("registerreceipt_/",register_receipt,name="registation"),
    path("registerloan_/",register_loan,name="registation"),
    path("registerreward_/",register_reward,name="registation"),









    
]