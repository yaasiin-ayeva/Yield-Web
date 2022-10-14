from django.shortcuts import render
from contacts.forms import PersonneForm, UploadCsvForm
from django.http import HttpResponseRedirect
import csv    
import io
import json
from contacts.models import Personne, Ville, Statut, MessageEnvoi, Eleve, Etablissement, Niveau
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse
from csv import reader
from pathlib import Path
import os
from django.views.decorators.csrf import csrf_protect

# Dear programmer after God come CODE. 
# Don't bother yourself if you have some misunderstanding, pray God and hope. 
# Sometimes The truth is what we can't know


# Create your views here.
def addpersonne(request):
	...
	#matiere = get_object_or_404(Matiere, id=id_mat)
	#eleve = get_object_or_404(Eleve, id_eleve=id_eleve)
	
	# if request.method == 'POST':
	# 	formObj = PersonneForm(request.POST)
	# 	if formObj.is_valid():
	# 		personne = Personne()
	# 		personne.nom = nom
	# 		personne.prenom = prenom
	# 		personne.sexe = formObj.cleaned_data['sexe']
	# 		personne.mobile = formObj.cleaned_data['mobile']
	# 		personne.indicatifTel = formObj.cleaned_data['indicatifTel']
	# 		personne.idVille = formObj.cleaned_data['idVille']
	# 		personne.idStatut = formObj.cleaned_data['idStatut']
	# 		personne.save()
	# 		return render(request, "personnes/personne_ajoutee.html")
	# else:
	# 	formObj =  PersonneForm()
	# ressources = {"formTmpl":formObj}
	# return render(request, "personnes/addpersonne.html", ressources)

# def ajoutCsv(request):
# 	if request.method == 'POST':
# 		print('un post')
# 	else:
# 		return render(request, "personnes/uploadCsv.html")

def handle_uploaded_file(f):
	print("handle")
	#print("dans with de handle")
	#ifile  = f.open()
	#read = csv.reader(ifile)
	# ifile = f.open()
	# fstring = read(ifile)
	# csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
	# print(read)
	# for i in range(len(csv_dicts)):
	# 	personne = Personne()

	# 	print(csv_dicts[i]['nom'])
	# 	# print(row[1])
	# 	# print(row[2])
	# 	# print(row[3])
	# 	# print(row[4])
	# 	# personne.nom = row[0]
	# 	# personne.prenom = row[1]
	# 	# personne.sexe = row[2]
	# 	# personne.mobile = row[2]
	# 	# personne.idVille = row[3]
	# 	# personne.idStatut = row[4]
	# 	# personne.save()
@login_required(login_url='/accounts/login/')
def uploadCsv(request):
	if request.method == 'POST':

		formCsv = UploadCsvForm(request.POST, request.FILES)
		print(formCsv.errors)
		if formCsv.is_valid():
			print('dans la méthode')
			print(request.FILES)
			with io.TextIOWrapper(request.FILES['file'], encoding="utf-8", newline='\n') as text_file:
				reader = csv.DictReader(text_file, delimiter=',')
				for row in reader:
					print(row['Ville'])
					if row['Tèl 1'] != '':
						personne = Personne()
						personne.nom = row['Nom']
						personne.prenom = row['Prénom']
						personne.sexe = row['sexe']
						personne.mobile = row['Tèl 1']
						personne.indicatifTel = row['indicatif']

						if row['Ville'] != '':
							if Ville.objects.filter(libelle=row['Ville']).exists():
								personne.idVille = Ville.objects.get(libelle=row['Ville'])
							else:
								ville = Ville()
								ville.libelle = row['Ville']
								ville.save()
								personne.idVille = ville
								
						if row['observation'] != '':
							if Statut.objects.filter(libelle=row['observation']).exists():
								personne.idStatut = Statut.objects.get(libelle=row['observation'])
							else:
								statut = Statut()
								statut.libelle = row['observation']
								print(row['observation'])
								statut.save()
								personne.idStatut = statut
						
						if row['Lycée'] != '':
							eleve = Eleve()
							
							eleve.nom = row['Nom']
							eleve.prenom = row['Prénom']
							eleve.sexe = row['sexe']
							eleve.mobile = row['Tèl 1']
							personne.indicatifTel = row['indicatif']
							if Etablissement.objects.filter(libelle=row['Lycée']).exists():
								eleve.idEtablissement = Etablissement.objects.get(libelle=row['Lycée'])
							else:
								etablissement = Etablissement()
								etablissement.libelle = row['Lycée']
								etablissement.save()
								eleve.idEtablissement = etablissement
								
								
							if row['Niveau'] != '':
								if Niveau.objects.filter(libelle=row['Niveau']).exists():
									eleve.idNiveau = Niveau.objects.get(libelle=row['Niveau'])
								else:
									niveau = Niveau()
									niveau.libelle = row['Niveau']
									niveau.save()
									eleve.idNiveau = niveau

							eleve.annee = row['année']
							print(personne)
							personne.save()
							eleve.idEleve = personne.idPersonne
							print(eleve)
							eleve.save()
						
					if row['Tèl 2'] != '':
						personne2 = Personne()
						personne2.nom = row['Nom']
						personne2.prenom = row['Prénom']
						personne2.sexe = row['sexe']
						personne2.mobile = row['Tèl 2']
						personne2.indicatifTel = row['indicatif']
						if row['Ville'] != '':
							if Ville.objects.filter(libelle=row['Ville']).exists():
								personne2.idVille = Ville.objects.get(libelle=row['Ville'])
							else:
								ville = Ville()
								ville.libelle = row['Ville']
								ville.save()
								personne2.idVille = ville
						if row['observation'] != '':
							if Statut.objects.filter(libelle=row['observation']).exists():
								personne2.idStatut = Statut.objects.get(libelle=row['observation'])
							else:
								statut = Statut()
								statut.libelle = row['observation']
								statut.save()
								personne2.idStatut = statut
								
					
						if row['Lycée'] != '':
							eleve2 = Eleve()
							
							eleve2.nom = row['Nom']
							eleve2.prenom = row['Prénom']
							eleve2.sexe = row['sexe']
							eleve2.mobile = row['Tèl 2']
							if Etablissement.objects.filter(libelle=row['Lycée']).exists():
								eleve2.idEtablissement = Etablissement.objects.get(libelle=row['Lycée'])
							else:
								etablissement = Etablissement()
								etablissement.libelle = row['Lycée']
								etablissement.save()
								eleve2.idEtablissement = etablissement

							
							if row['Niveau'] != '':
								if Niveau.objects.filter(libelle=row['Niveau']).exists():
									eleve2.idNiveau = Niveau.objects.get(libelle=row['Niveau'])
								else:
									niveau = Niveau()
									niveau.libelle = row['Niveau']
									niveau.save()
									eleve2.idNiveau = niveau
									
							eleve2.annee = row['année']
							print(personne2)
							personne2.save()
							eleve2.idEleve = personne2.idPersonne
							print(eleve2)
							eleve2.save()
						
			return HttpResponseRedirect('/success/url')
	else:
		formCsv = UploadCsvForm()
	return render(request, "personnes/uploadCsv.html", {"formCsv":formCsv})

class staticVar:
	nbReq = 0


@login_required(login_url='/accounts/login/')
def serveJson(request):
	try:
		#instance = staticVar()
		menvois = MessageEnvoi.objects.all().filter(statutEnvoi="A envoyer")
		listEnvois = list(menvois.values())
		#print(listEnvois)
		tab = []
		tab.append(listEnvois)
		aecrire = tab[staticVar.nbReq]
		with open('media/contact.json', 'w') as contact_file:
			json.dump(aecrire, contact_file)
			staticVar.nbReq+=1
		return HttpResponseRedirect('/media/contact.json')
	except IndexError:
		return HttpResponseRedirect('/success/url')

def homePage(request):
	return render(request, "projectT/index.html")