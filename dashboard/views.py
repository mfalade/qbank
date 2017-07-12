from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from accounts.models import AccountModel


# Create your views here.
class Dashboard(View):
    template_name = 'dashboard.html'
    items_limit = 15
    
    def get(self, request):
        accounts_qs = AccountModel.objects.order_by('-date_created')
        paginator = Paginator(accounts_qs, self.items_limit)
        accounts = paginator.page(1)
        context = {'accounts': accounts}
        return render(request, self.template_name, context)