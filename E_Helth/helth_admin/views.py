from django.shortcuts import render, redirect
from django.views.generic import View,CreateView
from .models import UserModel, MedicienandDiseasesModel
from .forms import UserForm, UserloginForm, MedicienanddiseasesForm
from django.contrib.auth import login, get_user_model, authenticate


# Create your views here.
def home(request):
    return render(request,"home.html")


def addUser(request):
    uform=UserForm
    uno=0
    try:
        res=UserModel.objects.all()[::-1][0]
        uno=res.uno+1
        return render(request, "adduser.html", {"form": uform, "value": UserModel.objects.all(), "idno": uno})
    except IndexError:
        uno=uno
        return render(request,"adduser.html")



def savedata(request):
    uno=request.POST.get("uno")
    uname = request.POST.get("uname")
    contact = request.POST.get("contact")
    uqty = request.POST.get("qualification")
    email = request.POST.get("email")
    proof = request.POST.get("proof")
    UserModel(uno=uno,uname=uname,contact=contact,qualification=uqty,email=email,proof=proof).save()
    return render(request,"adduser.html",{"value":UserModel.objects.all()})


def login_view(request):
    next=request.POST.get("next")
    form=UserloginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return render(request,"home.html")
    context={"form":form}
    return render(request,"login.html",context)


def updateuser(request):
    return render(request,"view.html",{"value":UserModel.objects.all()})


def updatuno(request):
    uno=request.POST.get('update')
    res=UserModel.objects.get(uno=uno)
    return render(request,"update.html",{"data":res,"form":UserForm})


def saveupdate(request):
    uno = request.POST.get("update")
    uname = request.POST.get("uname")
    contact = request.POST.get("contact")
    uqty = request.POST.get("qualification")
    email = request.POST.get("email")
    proof = request.POST.get("proof")
    UserModel(uno=uno,uname=uname,contact=contact,qualification=uqty,email=email,proof=proof).save()
    return updatuno(request)


def deleteuno(request):
    uno = request.POST.get("delete")
    UserModel.objects.get(uno=uno).delete()
    return updateuser(request)


def addmd(request):
    return render(request, "addmd.html", {"form":MedicienanddiseasesForm, "data": MedicienandDiseasesModel.objects.all()})


def savedatamd(request):
    dno = request.POST.get("mno")
    dname = request.POST.get("dname")
    medicines = request.POST.get("medicines")
    MedicienandDiseasesModel(mdno=dno, dname=dname, medicines=medicines).save()
    return render(request,"addmd.html",{"data":MedicienandDiseasesModel.objects.all()})


def viewmd(request):
    return render(request, "viewmd.html", {"data": MedicienandDiseasesModel.objects.all()})


def updatmd(request):
    updatemd=request.POST.get("updatemd")
    res=MedicienandDiseasesModel.objects.get(mdno=updatemd)
    return render(request,"updatemd.html",{"data":res,"form":MedicienanddiseasesForm})


def saveupdateMD(request):
    dno = request.POST.get("update")
    dname = request.POST.get("dname")
    medicines = request.POST.get("medicines")
    MedicienandDiseasesModel(mdno=dno, dname=dname, medicines=medicines).save()
    return viewmd(request)


def deletmd(request):
    mdno=request.POST.get("deletmd")
    MedicienandDiseasesModel.objects.get(mdno=mdno).delete()
    return viewmd(request)