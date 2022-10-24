from http import client
from ipaddress import ip_address
from random import choices
from django import forms
data_type=[('name','name'),('email','email'),('phone','phone'),('card_num','card_num'),('ip','ip')]
class loginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=100)
    password=forms.CharField(label='Password',max_length=100,widget=forms.PasswordInput)
class ResetPasswordForm(forms.Form):
    email=forms.EmailField(label='Email',max_length=100)
class ChangePasswordForm(forms.Form):
    old_password=forms.CharField(label='Old Password',max_length=100,widget=forms.PasswordInput)
    new_password=forms.CharField(label='New Password',max_length=100,widget=forms.PasswordInput)
    confirm_password=forms.CharField(label='Confirm Password',max_length=100,widget=forms.PasswordInput)
class baseForm(forms.Form):
    type=forms.CharField(label='Type',max_length=100,widget=forms.Select(choices=data_type))
    name=forms.CharField(label='Name',max_length=100)
    card_num=forms.CharField(label='Card Number',max_length=100)
    email=forms.CharField(label='Email',max_length=100)
    phone=forms.CharField(label='Phone',max_length=100)
    ip=forms.CharField(label='IP',max_length=100)
    
    {
        
    }
    
class BL_form(baseForm):
    merchant=forms.CharField(label='Merchant',max_length=100)

class GBL_form(baseForm):
    pass
class WL_form(BL_form):
    merchant=forms.CharField(label='Merchant',max_length=100)
class GWL_form(baseForm):
    pass

class Signup_form(forms.Form):
    
    username=forms.CharField(label='Username',max_length=100)
    email=forms.EmailField(label='Email',max_length=100)
    first_name=forms.CharField(label='First Name',max_length=100)
    last_name=forms.CharField(label='Last Name',max_length=100)
    
class Transaction_form(forms.Form):
    name=forms.CharField(label='Client Name',max_length=100)
    email=forms.EmailField(label='Client Email',max_length=100)
    phone=forms.CharField(label='Client Phone',max_length=100)
    card_num=forms.CharField(label='Client Card Number',max_length=100)
    ip=forms.CharField(label='Client IP',max_length=100)
    merchant=forms.CharField(label='Merchant',max_length=100)
    amount=forms.CharField(label='Amount',max_length=100)
    third_secure=forms.BooleanField(label='3rd Secure',required=True)