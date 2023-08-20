from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Enseignant
from .models import Materiel
from .models import Responsable
from .models import Budget
from .models import Passassion
from .models import Salle
from .models import Emprunt
from django.urls import reverse

from .forms import CreateEnseignantForm
from .forms import CreateMaterielForm
from .forms import CreateEmpruntForm
from .forms import CreatePassassionForm


# Create your views here.
def index(request):
    # template = loader.get_template('lycee/index.html')
    context = {}
    return render(request, 'lycee/index.html', context)


class CreateEnseignantView(CreateView):
    model = Enseignant
    form_class = CreateEnseignantForm
    template_name = 'lycee/enseignant/create.html'

    def get_success_url(self):
        return reverse("index")

class CreateMaterielView(CreateView):
    model = Materiel
    form_class = CreateMaterielForm
    template_name = 'lycee/materiel/create.html'

    def get_success_url(self):
        return reverse("index")

def InfoMaterielView(request):
    result_list = Materiel.objects.all
    responsable_list = Responsable.objects.all
    context = {'list': result_list, 'list_resp': responsable_list}
    return render(request, 'lycee/materiel/info.html', context)

def InfoEnseignantView(request):
    result_list = Enseignant.objects.all
    context = {'list': result_list}
    return render(request, 'lycee/enseignant/info.html', context)

class CreateEmpruntView(CreateView):
    model = Emprunt
    form_class = CreateEmpruntForm
    template_name = 'lycee/emprunt/create.html'

    def get_success_url(self):
        return reverse("index")


def CreatePassassionView(request):
    if request.method == 'POST':
        form = CreatePassassionForm(request.POST)
        if form.is_valid():
            passassion_instance = form.save()  # Enregistrez l'instance de Passassion

            # Mettez à jour l'attribut passassion de l'objet Emprunt associé
            emprunt_id = form.cleaned_data['emprunt'].id
            emprunt = Emprunt.objects.get(pk=emprunt_id)
            emprunt.passassion = True
            emprunt.save()

            return redirect('info_emprunt')  # Redirigez où vous voulez après la création
    else:
        form = CreatePassassionForm()

    context = {'form': form}
    return render(request, 'lycee/emprunt/create.html', context)

def InfoPassassionView(request):
    result_list = Passassion.objects.all
    enseignent_list = Enseignant.objects.all
    salle_list = Salle.objects.all
    context = {'list': result_list, 'enseignant_list': enseignent_list, 'salle_list': salle_list}
    return render(request, 'lycee/passassion/info.html', context)

def InfoEmpruntView(request):
    result_list = Emprunt.objects.all
    enseignent_list = Enseignant.objects.all
    materiel_list = Materiel.objects.all
    salle_list = Salle.objects.all
    context = {'list': result_list, 'enseignant_list': enseignent_list, 'salle_list': salle_list, 'materiel_list': materiel_list}
    return render(request, 'lycee/emprunt/info.html', context)