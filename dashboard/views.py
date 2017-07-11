from django.shortcuts import render
from django.views import View


# Create your views here.
class Dashboard(View):
    dashboard_template = 'dashboard.html'
    
    def get(self, request):
        return render(request, self.dashboard_template)