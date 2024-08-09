from django.shortcuts import render,redirect


# Create your views here.
from .forms import UsuarioForms, PropiedadForm

def index(request):
    return render(request, 'index.html')


def profile(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        u_form = UsuarioForms(instance=request.user)
    context={'u_form': u_form}
    return render(request, 'update_profile.html',context )


def crear_prop(request):
    if request.method == 'POST':
        
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PropiedadForm()
    context={'u_form': form}
    return render(request, 'new_propiedad.html',context )