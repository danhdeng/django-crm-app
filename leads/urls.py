from django.urls import path
from .views import lead_list, lead_details

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<pkey>', lead_details),
]
