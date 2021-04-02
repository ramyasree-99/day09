from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'ht/homepage.html')
def chk(request):
	return HttpResponse("<script>alert('hi GoodAfternoon')</script><h2>welcome</h2>")

def homepage(request):
    return render(request,'ht/homepage.html')

def lgn(re):
	return render (re,'ht/login.html')

def reg(rt):
	if rt.method=="POST":
		emailaddress=rt.POST['a']
		pas=rt.POST['b']
		ages=rt.POST['ag']
		return render(rt,'ht/homepage.html',{'info':emailaddress,'info2':pas})
	return render(rt,'ht/register.html')

def bthm(bt):
	return render(bt,'ht/bthm.html')

def about(ab):
	return render(ab,'ht/about.html')

def cont(cn):
	return render(cn,'ht/cont.html')