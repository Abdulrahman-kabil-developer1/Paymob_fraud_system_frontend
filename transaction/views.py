from django.shortcuts import render,redirect
import requests
from django.conf import settings
from transaction.forms import *
from django.contrib import messages
# Create your views here.
#BL --> Black List
#GBL --> Global Black List
#WL --> White List
#GWL --> Global White List
def list_transactions(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/list/transaction'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_transaction.html',{'transactions':response_data})
    else:
        return redirect('transaction:login')   

def list_review_transactions(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/list/review'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_review_transaction.html',{'transactions':response_data})
    else:
        return redirect('transaction:login')   

def send_transaction(request):
    if (request.COOKIES.get('auth_token')):
        if (request.method=='POST'):
            form=Transaction_form(request.POST)
            if (form.is_valid()):
                name=form.cleaned_data['name']
                card_num=form.cleaned_data['card_num']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone']
                ip=form.cleaned_data['ip']
                merchant=form.cleaned_data['merchant']
                amount=form.cleaned_data['amount']
                
                backend_url=settings.BACKEND_URL+'/send/transaction'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'name':name,'card_num':card_num,'email':email,'ip':ip,'phone':phone,'merchant':merchant,'amount':amount}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if (response_data['status']=='success'):
                    messages.success(request,"Transaction Acceopted")
                    messages.success(request,response_data['message'])
                else:
                    messages.warning(request,"Fraud Detected")
                    messages.warning(request,response_data['message'])
                return redirect('transaction:send_transaction')
        else:
            form=Transaction_form()
        return render(request,'send_transaction.html',{'form':form})
    else:
        return redirect('transaction:login')           
def list_BL(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/add/blacklist'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_BL.html',{'BL':response_data})
    else:
        return redirect('transaction:login')
def list_WL(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/add/whitelist'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_WL.html',{'WL':response_data})
    else:
        return redirect('transaction:login')
def list_GBL(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/add/global/blacklist'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_GBL.html',{'GBL':response_data})
    else:
        return redirect('transaction:login')
def list_GWL(request):
    if (request.COOKIES.get('auth_token')):
        backend_url=settings.BACKEND_URL+'/add/global/whitelist'
        headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
        response=requests.get(backend_url,headers=headers)
        response_data=response.json()
        if response.status_code==200:
            return render(request,'list_GWL.html',{'GWL':response_data})
    else:
        return redirect('transaction:login')

def add_to_BL(request):
    if (request.COOKIES.get('auth_token')):
        if (request.method=='POST'):
            form=BL_form(request.POST)
            if (form.is_valid()):
                type=form.cleaned_data['type']
                name=form.cleaned_data['name']
                card_num=form.cleaned_data['card_num']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone']
                ip=form.cleaned_data['ip']
                merchant=form.cleaned_data['merchant']
                backend_url=settings.BACKEND_URL+'/add/blacklist'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'type':type,'name':name,'card_num':card_num,'email':email,'ip':ip,'phone':phone,'merchant':merchant}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if (response_data['status']=='success'):
                    form.full_clean()
                    messages.success(request,response_data['message'])
                    return render(request,'add_to_BL.html',{'form':form})
                else:
                    messages.warning(request,response_data['message'])
                
        else:
            form=BL_form()
        return render(request,'add_to_BL.html',{'form':form})
    else:
        return redirect('transaction:login')
def add_to_GBL(request):
    if (request.COOKIES.get('auth_token')):
        if (request.method=='POST'):
            form=GBL_form(request.POST)
            if (form.is_valid()):
                type=form.cleaned_data['type']
                name=form.cleaned_data['name']
                card_num=form.cleaned_data['card_num']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone']
                ip=form.cleaned_data['ip']
                backend_url=settings.BACKEND_URL+'/add/global/blacklist'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'type':type,'name':name,'card_num':card_num,'email':email,'phone':phone,'ip':ip}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if (response_data['status']=='success'):
                    form.full_clean()
                    messages.success(request,response_data['message'])
                    return render(request,'add_to_GBL.html',{'form':form})
                else:
                    messages.warning(request,response_data['message'])
        else:  
            form=GBL_form()
        return render(request,'add_to_GBL.html',{'form':form})
    else:
        return redirect('transaction:login')
                
def add_to_WL(request):
    if (request.COOKIES.get('auth_token')):
        if (request.method=='POST'):
            form=WL_form(request.POST)
            if (form.is_valid()):
                type=form.cleaned_data['type']
                name=form.cleaned_data['name']
                card_num=form.cleaned_data['card_num']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone']
                ip=form.cleaned_data['ip']
                merchant=form.cleaned_data['merchant']
                backend_url=settings.BACKEND_URL+'/add/whitelist'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'type':type,'name':name,'card_num':card_num,'email':email,'phone':phone,'merchant':merchant,'ip':ip}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if (response_data['status']=='success'):
                    form.full_clean()
                    messages.success(request,response_data['message'])
                    return render(request,'add_to_BL.html',{'form':form})
                else:
                    messages.warning(request,response_data['message'])
        else:
            form=WL_form()
        return render(request,'add_to_WL.html',{'form':form})
    else:
        return redirect('transaction:login')
def add_to_GWL(request):
    if (request.COOKIES.get('auth_token')):
        if (request.method=='POST'):
            form=GWL_form(request.POST)
            if (form.is_valid()):
                type=form.cleaned_data['type']
                name=form.cleaned_data['name']
                card_num=form.cleaned_data['card_num']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone']
                ip=form.cleaned_data['ip']
                backend_url=settings.BACKEND_URL+'/add/global/whitelist'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'type':type,'name':name,'card_num':card_num,'email':email,'phone':phone,'ip':ip}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if (response_data['status']=='success'):
                    form.full_clean()
                    messages.success(request,response_data['message'])
                    return render(request,'add_to_GWL.html',{'form':form})
                else:
                    messages.warning(request,response_data['message'])
        else:
            form=GWL_form()
        return render(request,'add_to_GWL.html',{'form':form})
    else:
        return redirect('transaction:login')
                 
def login(request):
    if(not request.COOKIES.get('auth_token')):    
        form=loginForm()
        if (request.method=='POST'):
            form=loginForm(request.POST)
            if(form.is_valid()):
                recapcha_response=request.POST.get('g-recaptcha-response')
                data={
                    'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response' :recapcha_response
                }
                rechapch_request=requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                rechapch_result=rechapch_request.json()
                if(rechapch_result['success']):
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    backend_url=settings.BACKEND_URL+'/login'
                    headers={'Cotent-Type':'application/json'}
                    body={'username':username,'password':password}
                    response=requests.post(backend_url,headers=headers,data=body)
                    #save token in cookies
                    response_data=response.json()
                    
                    if (response_data['status']=='success'):
                        response=redirect('transaction:home')
                        response.set_cookie('username',(str(response_data['userInfo'].get('first_name'))+" "+str(response_data['userInfo'].get('last_name'))))
                        response.set_cookie('auth_token',response_data['token'])
                        messages.success(request,'Login Success')
                        messages.info(request,'Enjoy '+response_data['userInfo'].get('first_name')+" "+response_data['userInfo'].get('last_name'))
                        redirect('transaction:home')
                        return response
                    else:
                        messages.error(request,response_data['message'])
                        return redirect('transaction:login')
                
                    
                else:
                    messages.error(request,'Invalid reCAPTCHA. Please try again.')
            else:
                messages.error(request,form.errors)
        else:
            form=loginForm()
        context={'form':form}
        return render(request,'login.html',context)
    else:
        messages.info(request,'You are already logged in')
        return redirect('transaction:home')
def signup(request):
    form=Signup_form()
    if (request.method=='POST'):
        form=Signup_form(request.POST)
        if (form.is_valid()):
            recapcha_response=request.POST.get('g-recaptcha-response')
            data={
                'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' :recapcha_response
            }
            rechapch_request=requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            rechapch_result=rechapch_request.json()
            if(rechapch_result['success']):
                username=form.cleaned_data['username']
                email=form.cleaned_data['email']
                first_name=form.cleaned_data['first_name']
                last_name =form.cleaned_data['last_name']
                backendurl=settings.BACKEND_URL+'/signup'
                body={'username':username,'email':email,'first_name':first_name,'last_name':last_name}
                response=requests.post(backendurl,json=body)
                response_data=response.json()
                #check if response data hve key status
                
                if("status" in response_data and response_data['status']=='success'):
                    messages.success(request,response_data['message'])
                    return redirect('transaction:login')
                else:
                    messages.error(request,response_data)
            else:
                messages.error(request,'Invalid reCAPTCHA. Please try again.')
        else:
            messages.error(request,form.errors)
    else:
        form=Signup_form()
        
    return render(request,'signup.html',{'form':form})
def change_password(request):  
    if (request.COOKIES.get('auth_token') ):
    #print(request.COOKIES.get('auth_token'))
        form=ChangePasswordForm()
        if (request.method=='POST'):
            form=ChangePasswordForm(request.POST)
            print("post")
            if (form.is_valid()):
                old_password=form.cleaned_data['old_password']
                password=form.cleaned_data['new_password']
                confirm_password=form.cleaned_data['confirm_password']
                print("valid")
                backend_url=settings.BACKEND_URL+'/change/password'
                headers={'Authorization':'Token '+request.COOKIES.get('auth_token')}
                body={'old_password':old_password,'password':password,'confirm_password':confirm_password}
                response=requests.post(backend_url,headers=headers,json=body)
                response_data=response.json()
                if('status' in response_data and response_data['status']=='success'):
                    print("success")
                    messages.success(request,response_data['message'])
                    response=redirect('transaction:login')
                    response.delete_cookie('auth_token')
                    return response
                else:
                    print("error")
                    messages.error(request,response_data['message'])
                    return redirect('transaction:change_password')
            else:
                messages.error(request,form.errors)
                return redirect('transaction:change_password')
        else:
            form=ChangePasswordForm()
        return render(request,'change_password.html',{'form':form})
    else:
        messages.error(request,'Please login first')
        return redirect('transaction:login')
    
def reset_password(request):
    form=ResetPasswordForm()
    if(request.method=='POST'):
        form=ResetPasswordForm(request.POST)
        if (form.is_valid()):
            print("valid")
            email=form.cleaned_data['email']
            url=settings.BACKEND_URL+'/reset/password'
            body={'email':email}
            response=requests.post(url,json=body)
            if ("status" in response.json() and response.json()['status']=='success'):
                print("success")
                messages.success(request,response.json()['message'])
                return redirect('transaction:login')
            else:
                print("error")
                messages.error(request,response.json()['message'])
        else:
            messages.error(request,form.errors)
    else:
        form=ResetPasswordForm()
    return render(request,'reset_password.html',{'form':form})
    
        
def logout(request):
    if (request.COOKIES.get('auth_token')):
        response=redirect('transaction:home')
        response.delete_cookie('auth_token')
        response.delete_cookie('username')
        messages.success(request,'Logout Success')
        return response
    else:
        messages.error(request,'You are not logged in')
        return redirect('transaction:home')
def home(request):
    return render(request,'index.html')
