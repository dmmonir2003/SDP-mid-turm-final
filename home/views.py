from django.shortcuts import render ,redirect
from . import forms
from django.views.generic import ListView,DetailView
from .models import Car,CarBrand,Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

class HomePage(ListView):
    model=Car
    template_name='home.html'
    context_object_name ='cars'

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['car_brands']=CarBrand.objects.all()
        return context

class BrandCarListView(ListView):
    model = CarBrand
    template_name = 'home.html'
    context_object_name = 'cars'
    slug_url_kwarg = 'brand_name'

    def get_queryset(self):
        brand_name = self.kwargs.get(self.slug_url_kwarg)
        queryset = Car.objects.filter(brand__brand_name=brand_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_brands'] = CarBrand.objects.all()  
        return context

class details(DetailView):
    model=Car
    context_object_name='car'
    template_name='detail_car.html'

    def post(self,request,*args, **kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        car_comments=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.car_comments=car_comments
            new_comment.save()
        return HttpResponseRedirect(reverse('details_car', kwargs={'pk': car_comments.pk}))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_comments = self.object 
        comments =car_comments.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


        
@login_required
def buy_car(request,id):
    car=Car.objects.get(pk=id)
    if car.car_quantity>0:
      Cart.objects.create(user=request.user,car=car, quantity=1)
      car.car_quantity -=1
      car.save()
      return redirect('details_car',pk=id)
    else:
        messages.error(request,'Car not Available')
        return redirect('details_car',pk=id)




    


    
