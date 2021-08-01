from django.urls import path
from .views import (lead_list, lead_details, lead_create, lead_update, lead_delete, 
                    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView )

app_name = 'leads'

urlpatterns = [
    # path('', lead_list, name='lead-list'),
    
    # path('<int:pkey>/', lead_details, name='lead-details'),
    # path('create/', lead_create, name='lead-create'),
    # path('<int:pkey>/update/', lead_update, name='lead-update'),
    # path('<int:pkey>/delete/', lead_delete, name='lead-delete'),
    
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pkey>/', LeadDetailView.as_view(), name='lead-details'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pkey>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pkey>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    
]
