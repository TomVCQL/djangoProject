from django.forms import SelectDateWidget
from django.forms.models import ModelForm
from django import forms
from .models import Enseignant
from .models import Emprunt
from .models import Materiel
from .models import Passassion


class CreateEnseignantForm(ModelForm):

    class Meta:
        model = Enseignant
        fields = (
            "id",
            "nom",
            "prenom",
        )

class CreateMaterielForm(ModelForm):

    class Meta:
        model = Materiel
        fields = (
            "id",
            "type_materiel",
            "budget",
            "responsable",
            "salle_actuelle"
        )

class CreateEmpruntForm(ModelForm):
    date_emprunt = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    date_retour = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    class Meta:
        model = Emprunt
        fields = (
            "id",
            "date_emprunt",
            "date_retour",
            "object",
            "passassion",
            "enseignant",
            "materiel",
            "salle"
        )

class CreatePassassionForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

    class Meta:
        model = Passassion
        fields = (
            "id",
            "date",
            "objectif",
            "donneur",
            "receveur",
            "emprunt",
            "lieu"
        )
# class CursusCallForm(forms.Form):
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
#     students = forms.MultipleChoiceField(label='students', widget=forms.CheckboxSelectMultiple)
#
#     def __init__(self, cursus_id, *args, **kwargs):
#         super(CursusCallForm, self).__init__(*args, **kwargs)
#         self.fields['students'].choices = [(student.id, student.first_name+" "+student.last_name) for student in Student.objects.filter(cursus_id=cursus_id)]

