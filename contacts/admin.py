from django.contrib import admin
from contacts.models import Personne, Eleve, Message, Envoi, Etablissement, Niveau, Statut, Ville, MessageEnvoi

admin.site.site_title = 'Application Yield'
admin.site.site_header = 'Yield'

# Register your models here.
class EnvoiAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		#print(obj.idMessage)
		
		if obj.idEtablissement != None and obj.idNiveau != None:
			eleves = Eleve.objects.all()
			listEnvoi = []
			for e in eleves:
				if e.idEtablissement == obj.idEtablissement and e.idNiveau == obj.idNiveau:
					listEnvoi.append(e)
			for e in listEnvoi:
				message = obj.idMessage
				texteMessage = message.texteMessage
				menv = MessageEnvoi()
				menv.statutEnvoi = obj.statutEnvoi
				menv.idPersonne = Eleve.objects.get(idEleve=e.idEleve)
				menv.indicatif = e.indicatifTel
				texteMessage = texteMessage.replace("$nom$", e.nom)
				texteMessage = texteMessage.replace("$prenom$", e.prenom)
				niveau = obj.idNiveau
				texteMessage = texteMessage.replace("$niveau$", niveau.libelle)
				etablissement = obj.idEtablissement
				texteMessage = texteMessage.replace("$etablissement$", etablissement.libelle)
				menv.texteMessage = texteMessage
				menv.mobile = e.mobile
				menv.save()
		elif obj.idEtablissement != None and obj.idNiveau == None:
			eleves = Eleve.objects.all()
			listEnvoi = []
			for e in eleves:
				if e.idEtablissement == obj.idEtablissement:
					listEnvoi.append(e)
			for e in listEnvoi:
				message = obj.idMessage
				texteMessage = message.texteMessage
				menv = MessageEnvoi()
				menv.statutEnvoi = obj.statutEnvoi
				menv.idPersonne = Eleve.objects.get(idEleve=e.idEleve)
				menv.indicatif = e.indicatifTel
				texteMessage = texteMessage.replace("$nom$", e.nom)
				texteMessage = texteMessage.replace("$prenom$", e.prenom)
				etablissement = obj.idEtablissement
				texteMessage = texteMessage.replace("$etablissement$", etablissement.libelle)
				#texteMessage = texteMessage.replace("$niveau$", Niveau.objects.get(idNiveau=e.idNiveau).libelle)
				menv.texteMessage = texteMessage
				menv.mobile = e.mobile
				menv.save()
		elif obj.idNiveau != None and obj.idEtablissement == None:
			eleves = Eleve.objects.all()
			listEnvoi = []
			for e in eleves:
				if e.idNiveau == obj.idNiveau:
					listEnvoi.append(e)
			for e in listEnvoi:
				message = obj.idMessage
				texteMessage = message.texteMessage
				menv = MessageEnvoi()
				menv.statutEnvoi = obj.statutEnvoi
				menv.idPersonne = Eleve.objects.get(idEleve=e.idEleve)
				menv.indicatif = e.indicatifTel
				texteMessage = texteMessage.replace("$nom$", e.nom)
				texteMessage = texteMessage.replace("$prenom$", e.prenom)
				niveau = obj.idNiveau
				texteMessage = texteMessage.replace("$niveau$", niveau.libelle)
				print(texteMessage)
				menv.texteMessage = texteMessage
				menv.mobile = e.mobile
				menv.save()
		if obj.idVille != None:
			personnes = Personne.objects.all()
			listEnvoi = []
			for p in personnes:
				if p.idVille == obj.idVille:
					listEnvoi.append(p)
			for p in listEnvoi:
				message = obj.idMessage
				texteMessage = message.texteMessage
				menv = MessageEnvoi()
				menv.statutEnvoi = obj.statutEnvoi
				menv.idPersonne = Personne.objects.get(idPersonne=p.idPersonne)
				menv.indicatif = p.indicatifTel
				ville = obj.idVille
				texteMessage = texteMessage.replace("$nom$", p.nom)
				texteMessage = texteMessage.replace("$prenom$", p.prenom)
				texteMessage = texteMessage.replace("$ville$",ville.libelle)
				texteMessage = texteMessage.replace("$etablissement$", obj.idVille.libelle)
				#texteMessage = texteMessage.replace("$niveau$", Niveau.objects.get(idNiveau=e.idNiveau).libelle)
				print(texteMessage)
				menv.texteMessage = texteMessage
				menv.mobile = p.mobile
				menv.save()

		super().save_model(request, obj, form, change)		



admin.site.register(Ville)
admin.site.register(Statut)
admin.site.register(Etablissement)
admin.site.register(Niveau)
admin.site.register(Personne)
admin.site.register(Eleve)
admin.site.register(Message)
admin.site.register(Envoi, EnvoiAdmin)
admin.site.register(MessageEnvoi)