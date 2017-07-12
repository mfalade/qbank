from django.conf.urls import url, include

from accounts.views import AccountView, AccountDeleteView, AccountUpdateView


urlpatterns = [
    url(r'^create$', AccountView.as_view(), name='account_create'),
    url(r'^(?P<pk>\d+)/edit$', AccountUpdateView.as_view(), name='account_edit'),
    url(r'^(?P<pk>\d+)/delete$', AccountDeleteView.as_view(), name='account_delete'),
]