from django.shortcuts import render

# Create your views here.

def jobcategory(request):
    return render(request, 'preview/category.html')

def joblisting(request):
    return render(request, 'preview/job-listing2.html')

def pricingplan(request):
    return render(request, 'preview/pricing-plan.html')

def faq(request):
    return render(request, 'preview/faq.html')

def companylisting(request):
    return render(request, 'preview/company-listing2.html')

def blog(request):
    return render(request, 'preview/blog-grid.html')

def blogright(request):
    return render(request, 'preview/blog-right-sidebar.html')

def contact(request):
    return render(request, 'preview/contact.html')