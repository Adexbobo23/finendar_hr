from django.urls import path
from .views import (
    jobcategory, joblisting, pricingplan, faq,
    companylisting, blog, blogright, contact
)

urlpatterns = [ 
    path('job-category', jobcategory, name='job-category'),
    path('job-listing', joblisting, name='job-listing'),
    path('pricing-plan', pricingplan, name='pricing-plan'),
    path('faq', faq, name='faq'),
    path('company-listing', companylisting, name='company-listing'),
    path('blog', blog, name='blog-grid'),
    path('blog-side', blogright, name='blog-side'),
    path('contact', contact, name='contact'),
]