from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import UserForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.views.generic import ListView
from home.models import Cart,Car
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
     if not request.user.is_authenticated:
           if request.method=='POST':
              form=AuthenticationForm(request=request,data=request.POST)
              if form.is_valid():
                    name=form.cleaned_data['username']
                    user_pass=form.cleaned_data['password']
                    user=authenticate(username=name,password=user_pass)
                    if user is not None:
                           messages.success(request,'user login successfully !!')
                           login(request,user)
                           return redirect('home_page')
                    else:
                        messages.error(request,'Invalid username or password')
                        
              else:
                     form=AuthenticationForm()
                     return render(request,'form.html',{'form': form, 'type': 'Login'})      
           else:    
             form=AuthenticationForm()
             return render(request,'form.html',{'form': form, 'type': 'Login'})
     else:
        return redirect('home_page')
     
def user_signup(request):
        if not request.user.is_authenticated:
             if request.method=='POST':
                form=UserForm(request.POST)
                if form.is_valid():
                    messages.success(request,'user created successfully !! please login now')
                    form.save()
                    return redirect('user_login')
                else:
                   messages.error(request, 'Please correct the field .')
             
                   return render(request, 'form.html', {'form': form, 'type':   'Signup'})
              
             else:
              form=UserForm()
              return render(request,'form.html',{'form': form, 'type': 'Signup'})
             
        else:
            return redirect('home_page')
        
class user_profile(ListView):
    model = Cart
    template_name = 'profile.html'
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    

def user_profile_edit(request):
     if  request.user.is_authenticated:
           if request.method=='POST':
              form=UserUpdateForm(request.POST,instance=request.user)
              if form.is_valid():
                 form.save()
                 messages.success(request,'Profile Update successfully !!')
                 return redirect('home_page')
              
           else:    
              form=UserUpdateForm(instance=request.user)
              return render(request,'form.html',{'form': form, 'type': 'Profile Edit'})
     else:
        return redirect('home_page')

def password_update(request):
    if  request.user.is_authenticated:
           if request.method=='POST':
              form=PasswordChangeForm(user=request.user,data=request.POST)
              if form.is_valid():
                 form.save()
                 messages.success(request,'Password Update successfully !!')
                 update_session_auth_hash(request,form.user)
                 return redirect('home_page')
              else:
                  messages.error(request,'InValid Data')
                  form=PasswordChangeForm(user=request.user,data=request.POST)
                  return render(request,'form.html',{'form': form, 'type': 'Password Edit'})
           else:    
              form=PasswordChangeForm(user=request.user,data=request.POST)
              return render(request,'form.html',{'form': form, 'type': 'Password Edit'})
    else:
        return redirect('home_page')
    
@login_required
def remove_cart(request,id):
    cart=Cart.objects.filter(pk=id)
    cart.delete()
    return redirect('user_profile')
    
def user_logout(request):
    logout(request)
    return redirect('home_page')
        

