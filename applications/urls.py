from django.urls import path
from .views import (
    jobcategory, joblisting, pricingplan, faq,
    companylisting, blog, blogright, contact,
    jobposting, joblistingOne
)

urlpatterns = [ 
    path('job-category', jobcategory, name='job-category'),
    path('job-listing', joblisting, name='job-listing'),
    path('job-listing-one', joblistingOne, name='joblist'),
    path('pricing-plan', pricingplan, name='pricing-plan'),
    path('faq', faq, name='faq'),
    path('company-listing', companylisting, name='company-listing'),
    path('blog', blog, name='blog-grid'),
    path('blog-side', blogright, name='blog-side'),
    path('contact', contact, name='contact'),
    path('job-post', jobposting, name='job-post'),
]