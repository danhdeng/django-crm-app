from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, SalesPerson, User
from .forms import LeadForm, LeadModelForm, UserForm

# Create your views here.
#class based view
class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class=UserForm
    def get_success_url(self):
        return reverse("login-page")
class landingpageview(TemplateView):
    template_name="leads/landing_page.html"

class LeadListView(LoginRequiredMixin,ListView):
    template_name="leads/lead_list.html"
    queryset=Lead.objects.all()
    context_object_name="leads"
    
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name="leads/lead_details.html"
    queryset=Lead.objects.all()
    context_object_name="lead"
    pk_url_kwarg = 'pkey'
    
class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        #TODO send email notification
        send_mail(
            subject="Lead had been created",
            message="Lead had been created, please go the site and view it",
            from_email="test@testemail.com",
            recipient_list=["huidh@yahoo.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name="leads/lead_update.html"
    queryset=Lead.objects.all()
    pk_url_kwarg = 'pkey'
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    
class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name="leads/lead_delete.html"
    queryset=Lead.objects.all()
    pk_url_kwarg = 'pkey'
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")

#function based views
def landing_page(request):
    return render(request, "leads/landing_page.html")

def lead_list(request):
    leads=Lead.objects.all()
    context={
        "leads":leads,
    }
    return render(request, "leads/lead_list.html", context=context)

def lead_details(request, pkey):
    lead=Lead.objects.get(id=pkey)
    context={
        "lead":lead,
    }
    return render(request, "leads/lead_details.html", context=context)

def lead_create(request):
    print(request.POST)
    form=LeadModelForm()
    if(request.method == "POST"):
        form=LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context ={
        "form": form
    }
    return render(request, "leads/lead_create.html", context=context)

def lead_update(request, pkey):
    lead=Lead.objects.get(id=pkey)
    form=LeadModelForm(instance=lead)
    if(request.method == "POST"):
        form=LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context ={
        "form": form,
        "lead":lead
    }
    return render(request, "leads/lead_update.html", context=context)

def lead_delete(request, pkey):
    lead=Lead.objects.get(id=pkey)
    lead.delete()
    return redirect('/leads')

def lead_create_customform(request):
    print(request.POST)
    form=LeadForm()
    if(request.method == "POST"):
        form=LeadForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            agent=SalesPerson.objects.first()
            Lead.objects.create(    
                    first_name=first_name, 
                    last_name=last_name, 
                    age=age, 
                    agent=agent)
            return redirect('/leads')
    context ={
        "form": form
    }
    return render(request, "leads/lead_create.html", context=context)
