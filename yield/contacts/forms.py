from django.forms import ModelForm
from contacts.models import Personne
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError
from django import forms

class PersonneForm(ModelForm):
	class Meta:
		model = Personne
		#labels = {"nom": "Nom de l'élève"}
		fields = '__all__'

	def clean(self):
		cleaned_data = super().clean()
		nom = cleaned_data['nom'].upper()
		cleaned_data['nom'] = nom
		prenom = cleaned_data['prenom']
		sexe = cleaned_data['sexe']
		mobile = cleaned_data['mobile']
		idVille = cleaned_data['idville']
		idStatut = cleaned_data['idstatut']
		
		
		# for m in matieres:
		# 	if not (m in niveau.matieres.all()):
		# 		raise ValidationError(gettext_lazy( m.nom + ' n\'est pas enseignée à ce niveau'))

class UploadCsvForm(forms.Form):
	file = forms.FileField()