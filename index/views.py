from django.shortcuts import render
from .models import doctor_profile_1 , category , place
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    doctors=doctor_profile_1.objects.all()
    categories=category.objects.all()
    address=place.objects.all()
    paginator = Paginator(doctors, 3)
    page = request.GET.get('page')
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    return render(request,'home/index.html',{'doctors':doctors ,'categories':categories , 'address':address })
def detail(request,slug):
    doctor1=doctor_profile_1.objects.get(slug=slug)
    categories=category.objects.all()
    address=place.objects.all()
    return render(request,'home/detail.html',{'doctor':doctor1 , 'categories':categories , 'address':address})
def search_res(request):
    l=request.GET['loc','']
    name1=request.GET['name']
    spec1=request.GET['spec']
    search_result=doctor_profile_1.objects.filter(
        Q(name__contains=name1) |
        Q(specialist_doctor__speialists__contains=spec1) |
        Q(address1__location__contains=l)

    )
    return render(request,'home/search_result.html',{'results':search_result})