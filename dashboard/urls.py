from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from dashboard.views import DashboardView


urlpatterns = [
    url(r'^$', login_required(DashboardView.as_view()), name='index'),
]