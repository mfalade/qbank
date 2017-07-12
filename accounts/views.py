from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, FormView, UpdateView

from accounts.forms import AccountForm
from accounts.models import AccountModel

class AccountView(FormView):
    template_name = 'account_create.html'
    form_class = AccountForm
    success_url = '/dashboard'

    def form_valid(self, form):
        form.save()
        return super(AccountView, self).form_valid(form)


class AccountDeleteView(DeleteView):
    model = AccountModel
    template_name = 'account_confirm_delete.html'
    success_url = reverse_lazy('dashboard')


class AccountUpdateView(UpdateView):
    model = AccountModel
    template_name = 'account_update.html'
    fields = '__all__'
