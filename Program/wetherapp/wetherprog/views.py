from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden
from wetherprog.models import WetherDB, DTO

wetherDB = WetherDB()

def user(request):
    datas = wetherDB.getAll()
    response = render(request, "user.html", context={"datas": datas})
    response.set_cookie("autor", "False")
    return response

def autor(request):
    passw = request.GET.get("Passw")
    if int(passw) != 123:
        return HttpResponseForbidden("Uncorect password")
    response = HttpResponseRedirect("/admin/")
    response.set_cookie("autor", "True")
    return response

def admin(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseForbidden("You is not admin")
    datas = wetherDB.getAll()
    return render(request, "admin.html", context={"datas": datas})

def add(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseForbidden("You is not admin")
    name = request.GET.get("Name")
    d = request.GET.get("D")
    m = request.GET.get("M")
    y = request.GET.get("Y")
    morn = request.GET.get("Morn")
    noon = request.GET.get("Noon")
    night = request.GET.get("Night")
    dto = DTO(0, str(name), int(d), int(m), int(y), int(morn), int(noon), int(night))
    wetherDB.add(dto)
    return HttpResponseRedirect("/admin/")

def up(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseForbidden("You is not admin")
    id = request.GET.get("Id")
    name = request.GET.get("Name")
    d = request.GET.get("D")
    m = request.GET.get("M")
    y = request.GET.get("Y")
    morn = request.GET.get("Morn")
    noon = request.GET.get("Noon")
    night = request.GET.get("Night")
    dto = DTO(int(id), str(name), int(d), int(m), int(y), int(morn), int(noon), int(night))
    req = wetherDB.update(dto)
    if req == None:
        return HttpResponseNotFound("Not found Day")
    return HttpResponseRedirect("/admin/")

def dele(request):
    autor = request.COOKIES["autor"]
    if autor == "False":
        return HttpResponseForbidden("You is not admin")
    id = request.GET.get("Id")
    req = wetherDB.delete(int(id))
    if req == None:
        return HttpResponseNotFound("Not found Day")
    return HttpResponseRedirect("/admin/")