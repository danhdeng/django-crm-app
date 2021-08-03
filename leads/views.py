from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, SalesPerson, User, Category
from .forms import LeadForm, LeadModelForm, UserForm, AssignAgentForm,LeadCategoryUpdateForm
from salesperson.mixins import OrganizerLoginRequiredMixin

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
    context_object_name="leads"
    
    def get_queryset(self):
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
           queryset =queryset.filter(organization=user.userprofile, agent__isnull=False) 
        else:
            queryset =queryset.filter(organization=user.salesperson.organization, agent__isnull=True)
            queryset =queryset.filter(agent__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
            queryset =queryset.filter(organization=user.userprofile, agent__isnull=True)
        context.update({
            "unassigned_leads": queryset
        })
        return context

     
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name="leads/lead_details.html"
    context_object_name="lead"
    pk_url_kwarg = 'pkey'
    
    def get_queryset(self):
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
           queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.agent.organization)
            queryset =queryset.filter(agent__user=user)
        return queryset    
    
class LeadCreateView(OrganizerLoginRequiredMixin, CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        lead=form.save(commit=False)
        lead.organization=self.request.user.userprofile
        lead.save()
        send_mail(
            subject="Lead had been created",
            message="Lead had been created, please go the site and view it",
            from_email="test@testemail.com",
            recipient_list=["huidh@yahoo.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
class LeadUpdateView(OrganizerLoginRequiredMixin, UpdateView):
    template_name="leads/lead_update.html"
    pk_url_kwarg = 'pkey'
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def get_queryset(self):
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
            queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.agent.organization)
            queryset =queryset.filter(agent__user=user)
        return queryset    
    
class LeadDeleteView(OrganizerLoginRequiredMixin, DeleteView):
    template_name="leads/lead_delete.html"
    pk_url_kwarg = 'pkey'
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    def get_queryset(self):
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
            queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.agent.organization)
            queryset =queryset.filter(agent__user=user)
        return queryset    
 
class AssignAgentView(OrganizerLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class=AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs=super(AssignAgentView, self).get_form_kwargs(**kwargs)    
        kwargs.update( {
            "request": self.request
        })
        return kwargs
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead=Lead.objects.filter(id =self.kwargs["pkey"]).first()
        lead.agent=agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

#View to handle Category
class CategoryListView(LoginRequiredMixin,ListView):
    template_name="leads/category_list.html"
    context_object_name="category_list"
    
    def get_queryset(self):
        user=self.request.user
        queryset =Category.objects.all()
        if user.is_organizer:
           queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.salesperson.organization)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
            queryset =queryset.filter(organization=user.userprofile)
        else:
            queryset =queryset.filter(organization=user.salesperson.organization)
        
        print(queryset)
        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context  
    
class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name="leads/category_details.html"
    context_object_name="category"
    pk_url_kwarg = 'pkey'
     
    def get_queryset(self):
        user=self.request.user
        queryset =Category.objects.filter()
        if user.is_organizer:
           queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.salesperson.organization)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        leads=self.get_object().leads.all()
        context.update({
            "leads": leads
        })
        return context  


class LeadCategoryUpdateView(OrganizerLoginRequiredMixin, UpdateView):
    template_name="leads/lead_category_update.html"
    pk_url_kwarg = 'pkey'
    form_class=LeadCategoryUpdateForm
    
    def get_success_url(self):
        return reverse("leads:lead-details", kwargs={"pkey": self.get_object().id})
    
    def get_queryset(self):
        user=self.request.user
        queryset =Lead.objects.all()
        if user.is_organizer:
            queryset =queryset.filter(organization=user.userprofile) 
        else:
            queryset =queryset.filter(organization=user.agent.organization)
            queryset =queryset.filter(agent__user=user)
        return queryset 

#function based views sections
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
