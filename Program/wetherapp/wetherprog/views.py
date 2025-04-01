from django.shortcuts import render
from django.http import HttpResponseRedirect
from wetherprog.models import Day, Date, Temp
from .forms import AdminForm

def user(request):
    days = Day.objects.select_related("date", "temp").all()
    response = render(request, "user.html", {"days": days})
    response.set_cookie("autor", "False")
    return response

def errmsguser(request, error="All good"):
    return render(request, "errmsguser.html", {"error": error})

def autor(request):
    passw = request.POST.get("Passw")
    if int(passw) != 123:
        return HttpResponseRedirect("/errmsguser/Invalid password")
    response = HttpResponseRedirect("/admin/")
    response.set_cookie("autor", "True")
    return response

def errmsgadmin(request, error="All good"):
    return render(request, "errmsgadmin.html", {"error": error})

def admin(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseRedirect("/errmsguser/You in not admin")
    adminForm = AdminForm(request.POST)
    days = Day.objects.select_related("date", "temp").all()
    return render(request, "admin.html", {"days": days, "form": adminForm})

def add(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseRedirect("/errmsguser/You in not admin")
    
    adminForm = AdminForm(request.POST)
    if adminForm.is_valid():      
        day = Day()
        date = Date()
        temp = Temp()
        date.Name = adminForm.cleaned_data["name"]
        date.D = adminForm.cleaned_data["d"]
        date.M = adminForm.cleaned_data["m"]
        date.Y = adminForm.cleaned_data["y"]
        date.save()

        temp.Morn = adminForm.cleaned_data["morn"]
        temp.Noon = adminForm.cleaned_data["noon"]
        temp.Night = adminForm.cleaned_data["night"]
        temp.save()

        day.date = date
        day.temp = temp  
        day.save()     
        return HttpResponseRedirect("/admin/")

def up(request, id:int):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseRedirect("/errmsguser/You in not admin")
    try:
        day = Day.objects.select_related("date", "temp").get(id=id)
        date:Date = day.date
        temp:Temp = day.temp
        adminForm = AdminForm(request.POST)
        if request.method == "POST":
            if adminForm.is_valid():
                date.Name = adminForm.cleaned_data["name"]
                date.D = adminForm.cleaned_data["d"]
                date.M = adminForm.cleaned_data["m"]
                date.Y = adminForm.cleaned_data["y"]
                date.save()

                temp.Morn = adminForm.cleaned_data["morn"]
                temp.Noon = adminForm.cleaned_data["noon"]
                temp.Night = adminForm.cleaned_data["night"]
                temp.save()
                return HttpResponseRedirect("/admin/")
        else:
            return render(request, "up.html", {"form": adminForm})
    except Day.DoesNotExist:
        return HttpResponseRedirect("/errmsgadmin/Day not found")

def dele(request, id:int):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseRedirect("/errmsguser/You in not admin")
    try:
        day = Day.objects.select_related("date", "temp").get(id=id)
        day.date.delete()
        day.temp.delete()
        day.delete()
        return HttpResponseRedirect("/admin/")
    except Day.DoesNotExist:
        return HttpResponseRedirect("/errmsgadmin/Day not found")