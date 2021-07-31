from django.shortcuts import render, redirect   
from django.http import HttpResponse
from .models import Lead, SalesPerson
from .forms import LeadForm, LeadModelForm

# Create your views here.

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
