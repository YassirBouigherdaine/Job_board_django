
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Job
from .form import ApplyForm, JobForm
from django.core.paginator import Paginator

# Create your views here.

def job_detail(request, slug):
    job_details = Job.objects.get(slug=slug)

    if request.method=='POST':
       form = ApplyForm(request.POST, request.FILES)
       if form.is_valid():
           jobForm = form.save(commit=False)
           jobForm.job = job_details
           jobForm.save()
        
    else:
        form = ApplyForm()
    
    context = {"job":job_details, 'form':form}
    return render(request, "job/job_details.html", context)


def jobs(request):
    jobs = Job.objects.all() 
    paginator = Paginator(jobs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"jobs": page_obj}
    return render(request, "job/jobs.html", context)


def add_job(request):

    if request.method=='POST':
       add_job_form = JobForm(request.POST, request.FILES)
       if add_job_form.is_valid():
           myForm = add_job_form.save(commit=False)
           myForm.user = request.user
           myForm.save()
           return redirect(reverse('jobs:jobs'))



    else:
        add_job_form = JobForm()
    

    return render(request, "job/add_job.html", {'add_job_form':add_job_form})