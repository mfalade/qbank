from django.conf.urls import url, include
from .views import Home, Login, Logout


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^pweet$', Logout.as_view(), name='nonsocial'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]