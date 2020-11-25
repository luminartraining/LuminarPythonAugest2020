from django.shortcuts import render, redirect
from accounts.models import Account
# Create your views here.
from accounts.forms import AccountCreateForm,LoginForm,BalanceChkform,TransferAmountForm


def transfer(request):
    form=TransferAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TransferAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            try:
                object = Account.objects.get(mpin=mpin)#1234(
                bal=object.balance-amount #3000-2000bal=1000
                object.balance=bal
                object.save()
            except Exception:
                context["form"] = form
                return render(request, "accounts/transferamount.html", context)

            form.save()
            return redirect("balance")
        else:
            context["form"]=form
            return render(request, "accounts/transferamount.html", context)
    return  render(request,"accounts/transferamount.html",context)
def createAccount(request):
    template_name="accounts/accountcreate.html"

    form=AccountCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=AccountCreateForm(request.POST)

        if form.is_valid():
            personname=form.cleaned_data.get("personname")
            accno=form.cleaned_data.get("accno")
            actype=form.cleaned_data.get("actype")
            balance=form.cleaned_data.get("balance")
            phonenumber=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")

            obj=Account(personname=personname,accno=accno,actype=actype,balance=balance,phonenumber=phonenumber,mpin=mpin)
            obj.save()
            return render(request, template_name, context)
    return render(request,template_name,context)







def loginView(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            phone=form.cleaned_data.get("phonenumber")#9526562826
            mpin=form.cleaned_data.get("mpin")#1234
            try:
                object=Account.objects.get(phonenumber=phone)
                if ((object.phonenumber == phone) & (object.mpin == mpin)):
                    print("user is exist")
                    return render(request,"accounts/accounthome.html")
            except Exception as e:
                print("invalid credentials")
                context["form"] = form
                return render(request, "accounts/login.html", context)


    return render(request,"accounts/login.html",context)


def balanceEnq(request):
    form=BalanceChkform()
    context={}
    context["form"] = form
    if request.method=="POST":
        form=BalanceChkform(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")#1234
            try:
                object=Account.objects.get(mpin=mpin)
                context["balance"]=object.balance
                return render(request,"accounts/checkbalance.html",context)
            except Exception as e:
                context["form"]=form
                return render(request, "accounts/checkbalance.html", context)

    return render(request,"accounts/checkbalance.html",context)






def accountActivity(request):
    form=BalanceChkform()
    context={}
    context["form"]=form
    return render(request,"accounts/accounthistory.html",context)
