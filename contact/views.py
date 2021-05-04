from django.shortcuts import render,redirect
from django.core.mail import send_mail
# Create your views here.
def contact_info(request):
    return render(request,'contact/contact.html')
def send(request):
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        mail =request.POST.get('mail')
        print(mail)
        subject=request.POST.get('subject')
        print(subject)
        messages=request.POST.get('messages')
        print(messages)
        send_mail(
            subject,
            f'sender name{name},sender mail{mail},subject{subject},message{messages}',
            mail,
            ['eng_mina_hosam@yahoo.com'],
            fail_silently=False,
        )
        return redirect('contact:contact')