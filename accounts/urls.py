from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from accounts.views import AccountView, AccountDeleteView, AccountUpdateView


urlpatterns = [
    url(r'^create$', login_required(AccountView.as_view()), name='account_create'),
    url(r'^(?P<pk>\d+)/edit$', login_required(AccountUpdateView.as_view()), name='account_edit'),
    url(r'^(?P<pk>\d+)/delete$', login_required(AccountDeleteView.as_view()), name='account_delete'),
]