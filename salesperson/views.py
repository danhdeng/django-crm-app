import random

from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from leads.models import SalesPerson
from salesperson.forms import SalesPersonForm
from .mixins import OrganizerLoginRequiredMixin
    
# Create your views here.
class SalesPersonListView(OrganizerLoginRequiredMixin, generic.ListView):
    template_name ="salesperson/sales_list.html"
    context_object_name="saleslist"
    
    def get_queryset(self):
        user_request_organization=self.request.user.userprofile
        return SalesPerson.objects.filter(organization=user_request_organization)

class SalesPersonCreateView(OrganizerLoginRequiredMixin, generic.CreateView):
    template_name ="salesperson/sales_create.html"
    form_class =SalesPersonForm
    
    def get_success_url(self):
        return reverse('salesperson:salesperson-list')
    
    def form_valid(self, form):
        user=form.save(commit=False)
        user.is_organizer=False
        user.is_agent=True
        user.set_password(f"{random.randint(0,100000)}")
        user.save()
        SalesPerson.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject="you are inviated to be an agent",
            message="please log into the portal to start work on the leads",
            from_email="admin@test.com",
            recipient_list=[user.email],
        )

        return super(SalesPersonCreateView, self).form_valid(form)
    
    
class SalesPersonDetailsView(OrganizerLoginRequiredMixin, generic.DetailView):
    template_name ="salesperson/sales_details.html"
    context_object_name="agent"
    pk_url_kwarg = 'pkey'
    
    def get_queryset(self):
        user_request_organization=self.request.user.userprofile
        return SalesPerson.objects.filter(organization=user_request_organization)
    
class SalesPersonUpdateView(OrganizerLoginRequiredMixin, generic.UpdateView):
    template_name ="salesperson/sales_update.html"
    form_class=SalesPersonForm
    context_object_name="agent"
    pk_url_kwarg = 'pkey'
    
    def get_queryset(self):
        user_request_organization=self.request.user.userprofile
        return SalesPerson.objects.filter(organization=user_request_organization)
    
    def get_success_url(self):
        return reverse('salesperson:salesperson-list')
    

class SalesPersonDeleteView(OrganizerLoginRequiredMixin, generic.DeleteView):
    template_name ="salesperson/sales_delete.html"
    form_class=SalesPersonForm
    pk_url_kwarg = 'pkey'
    
    def get_queryset(self):
        user_request_organization=self.request.user.userprofile
        return SalesPerson.objects.filter(organization=user_request_organization)
    
    def get_success_url(self):
        return reverse('salesperson:salesperson-list')
    