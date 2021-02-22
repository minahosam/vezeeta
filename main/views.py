from django.shortcuts import render
from .models import footer
# Create your views here.
def  footer_info(request):
    foot=footer.objects.last()
    return {'foot':foot}