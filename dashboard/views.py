from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.list import ListView

from accounts.models import AccountModel


class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = AccountModel
    context_object_name = 'accounts'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(**kwargs)