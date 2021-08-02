from django.urls import path
from .views import SalesPersonListView, SalesPersonCreateView, SalesPersonDetailsView, SalesPersonUpdateView,SalesPersonDeleteView

app_name = 'salesperson'

urlpatterns = [
    path('', SalesPersonListView.as_view(), name='salesperson-list'),
    path('create/', SalesPersonCreateView.as_view(), name='salesperson-create'),
    path('<int:pkey>/', SalesPersonDetailsView.as_view(), name='salesperson-details'),
    path('<int:pkey>/update/', SalesPersonUpdateView.as_view(), name='salesperson-update'),
    path('<int:pkey>/delete/', SalesPersonDeleteView.as_view(), name='salesperson-delete'),
]