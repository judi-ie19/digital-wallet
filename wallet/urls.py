from django.urls import path
from .views import register_account ,register_customer, register_transaction,register_wallet,register_account
 

urlpatterns=[
    path("register/",register_customer,name="registation"),
    path("registerwallet/",register_wallet,name="registation"),
    path("registeraccount/",register_account,name="registation"),
    path("registertransaction/",register_transaction,name="registation"),

    
]