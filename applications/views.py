from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job
from django.contrib import messages


def jobcategory(request):
    return render(request, 'preview/category.html')

def joblisting(request):
    jobs = Job.objects.all()
    return render(request, 'preview/job-listing2.html', {'jobs': jobs})

def joblistingOne(request):
    jobs = Job.objects.all()
    return render(request, 'preview/job-listing1.html', {'jobs': jobs})

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


@login_required(login_url='login')
def jobposting(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, 'Job post created successfully!')
            return redirect('job-listing')
        else:
            messages.error(request, 'Form is not valid. Please check the errors below.')
            print(form.errors) 
    else:
        form = JobForm()

    return render(request, 'preview/job-post.html', {'form': form})
