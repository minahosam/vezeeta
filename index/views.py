from django.shortcuts import redirect, render
from django.db.models import F,Sum,Avg
from .models import doctor_profile_1 , category, doctor_reservation , place , subscribed_mails,rate_doctor
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import reservation_form
from accounts.forms import new_user
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
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
    email2=request.POST.get('email1')
    print(email2)
    subscribed_mails.objects.create(email=email2)
    return render(request,'home/index.html',{'doctors':doctors ,'categories':categories , 'address':address})
def detail(request,slug):
    doctor1=doctor_profile_1.objects.get(slug=slug)
    categories=category.objects.all()
    address=place.objects.all()
    return render(request,'home/detail.html',{'doctor':doctor1 , 'categories':categories , 'address':address})
def search_res(request):
    l=request.GET['loc']
    name1=request.GET['name']
    spec1=request.GET['spec']
    search_result=doctor_profile_1.objects.filter(
        Q(address1__location__icontains=l) &        
        Q(specialist_doctor__speialists__icontains=spec1) &
        Q(name__icontains=name1)

    )
    return render(request,'home/search_result.html',{'results':search_result})
def reservation(request):
    if request.method == 'POST':
        reservation=reservation_form(request.POST, request.FILES)
        if reservation.is_valid():
            res1=reservation.save(commit=False)
            res1.name=request.user
            res1.email=request.user.email
            res1.save()
            messages.success(request,'تم الحجز بنجاح')
            return redirect('index:index')
    else:
        reservation=reservation_form()
    return render(request,'home/appointment.html',{'form2':reservation})
def subscribed_mail(request):
    email2=request.POST.get('email1')
    print(email2)
    subscribed_mails.objects.create(email=email2)
    return JsonResponse({'done':'done'})
def my_reservtion(request):
    reversation_user=request.user
    print(reversation_user)
    num_of_reservation=doctor_reservation.objects.filter(name=reversation_user)
    return render(request,'home/my_reservation.html',{'doctors':num_of_reservation})
def my_profile(request):
    user_profile_=request.user
    print(user_profile_)
    user_profile=doctor_profile_1.objects.get(user=user_profile_)
    return render(request,'home/profile.html',{'user':user_profile})
def rate(request):
    if request.method == 'GET':
        doctor_id=request.GET.get('doctor_id')
        print(doctor_id)
        rate_score=request.GET.get('score_id')
        print(rate_score)
        # id_of_the_rated_doctor=doctor_profile_1.objects.get(id=doctor_id)
        rated_doctor=rate_doctor.objects.get(id=doctor_id)
        rated_doctor.rate_value=rate_score
        rated_doctor.user_rated=request.user
        rated_doctor.save()
        return JsonResponse({'success':'true','rate_value':rate_score},safe=False)
    return JsonResponse({'success':'false'})