from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Login.forms import RegistrationForm
from Login.forms import createForm, RegistrationForm, resumeViewForm, resumeEditForm, resumeDeleteForm, \
    resumepublicForm

# Create your views here.
from Login.models import Create


def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('uname')
    password = request.POST.get('pwd')
    print (username, ",", password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login_view(request, user)
      return redirect("home")
    else:
      return redirect("login_view")
  return render(request, 'login.html')


def Register(request):
  form = RegistrationForm()
  context = {}
  context['form'] = form
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login_view')
    else:
      context = {}
      context['form'] = form
      return render(request, "registration.html", context)
  return render(request, "registration.html", context)


@login_required(login_url='login_view')
def home(request):
  return render(request, 'home.html')

def resumeCreate(request, pk):
  form = createForm(initial={'uid': pk, "user": request.user})
  context = {}
  context['form'] = form
  qs = Create.objects.all()
  context['obj'] = qs
  if request.method == "POST":
    form = createForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('createresume')
  return render(request, "createresume.html", context)

def resumeview(request, pk):
  qs = Create.objects.get(id=pk)
  context = {}
  context['user'] = qs
  return render(request, "resumeview.html", context)


def resumeEdit(request, pk):
  qs = Create.objects.get(id=pk)
  form = resumeEditForm(instance=qs)
  context = {}
  context["form"] = form
  if request.method == "POST":
    qs = Create.objects.get(id=pk)
    form = resumeEditForm(instance=qs, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect("createresume")
  return render(request, "resumeedit.html", context)


def resumeDelete(request, pk):
  product = Create.objects.get(id=pk)
  form = resumeDeleteForm(instance=product)
  context = {}
  context["form"] = form
  if request.method == "POST":
    product = Create.objects.get(id=pk)
    form = resumeDeleteForm(instance=product, data=request.POST)
    if form.is_valid():
      product.delete()

      return redirect("createresume")
  return render(request, "resumedelete.html", context)


def viewresume(request):
  obj = Create.objects.filter(user=request.user)
  context = {}
  context['obj'] = obj
  return render(request, "resumepublic.html", context)


def resumedetails(request, pk):
  qs = Create.objects.get(id=pk)
  context = {}
  context['obj'] = qs
  return render(request, "publicview.html", context)