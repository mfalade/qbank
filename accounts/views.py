from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import DeleteView, FormView, UpdateView

from accounts.forms import AccountForm
from accounts.models import AccountModel


class AccountView(FormView):
    form_class = AccountForm
    template_name = 'accounts/account_create.html'
    success_url = '/dashboard'

    def form_valid(self, form):
        account_instance = form.save(commit=False)
        account_instance.creator = self.request.user
        account_instance.save()
        return super(AccountView, self).form_valid(form)


class UserPermissionMixin(object):
    """Ensures only authorized users can perform specific actions.

    Restricts manipulation or deleting of an account to either the 
    super admin, or the user that created the account.
    """
    def get_object(self, queryset=None):
        account = super(UserPermissionMixin, self).get_object()
        user = self.request.user
        if any([account.creator == user, user.is_superuser]):
            return account
        raise PermissionDenied


class AccountDeleteView(UserPermissionMixin, DeleteView):
    model = AccountModel
    form_class = AccountForm
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('dashboard:index')


class AccountUpdateView(UserPermissionMixin, UpdateView):
    model = AccountModel
    form_class = AccountForm
    template_name = 'accounts/account_update.html'
    success_url = reverse_lazy('dashboard:index')
