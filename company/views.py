from django.shortcuts import render

# Create your views here.
def company_dashboard(request):
    return render(request, 'creator/creator_dashboard.html')