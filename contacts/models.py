from django.db import models

# Create your models here.
class Statut(models.Model):
	idStatut = models.AutoField(primary_key=True)
	libelle = models.CharField(max_length=600)
	def __str__(self):
		return 'Statut: ' + self.libelle

class Ville(models.Model):
	idVille = models.AutoField(primary_key=True)
	libelle = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return 'La ville de ' + self.libelle

class Personne(models.Model):
	idPersonne = models.AutoField(primary_key=True)
	MASCULIN = 'M'
	FEMININ = 'F'
	sexe_choices = [
		(MASCULIN, 'Masculin'),
		(FEMININ, 'Feminin')
	]
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	sexe = models.CharField(max_length=8, choices=sexe_choices, null=True, blank=True)
	#date_naissance = models.DateField()
	#utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	indicatifTel = models.CharField(null=True, default='+228', max_length=4)
	mobile = models.CharField(max_length=15, null=True)
	idVille = models.ForeignKey(Ville, on_delete=models.CASCADE, unique=False, null=True, blank=True)
	idStatut = models.ForeignKey(Statut, on_delete=models.CASCADE, unique=False, null=True, blank=True)

	class Meta:
		abstract = False

	def __str__(self):
		return 'Le nom de la personne est: ' + self.nom + '. Son prenom est: ' + self.prenom

class Niveau(models.Model):
	idNiveau = models.AutoField(primary_key=True)
	libelle = models.CharField(max_length=20, unique=True)
	
	def __str__(self):
		return 'Classe de ' + self.libelle

class Etablissement(models.Model):
	idEtablissement = models.AutoField(primary_key=True)
	libelle = models.CharField(max_length=50)
	def __str__(self):
		return 'École ' + self.libelle



class Eleve(Personne):
	idEleve = models.AutoField(primary_key=True)
	idNiveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, unique=False, null=True, blank=True)
	idEtablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, unique=False, null=True, blank=True)
	annee = models.IntegerField(null=True, blank=True)
	def __str__(self):
		return  self.nom + ' ' + self.prenom


class Message(models.Model):
	idMessage = models.AutoField(primary_key=True)
	texteMessage = models.TextField(max_length=6700)
	def __str__(self):
		return 'Texte du message: ' + self.texteMessage[0:25]

class Envoi(models.Model):
	aEnv = 'A envoyer'
	env = 'Envoyé'
	recu = 'Reçu'
	lu = 'Lu'
	envoi_choices = [
		(aEnv, 'A envoyer'),
		(env, 'Envoyé'),
		(recu, 'Reçu'),
		(lu, 'Lu')]
	idEnvoi = models.AutoField(primary_key=True)
	statutEnvoi = models.CharField(max_length=50, choices=envoi_choices, default='A envoyer')
	#dateCreation = models.DateField()
	#personne = models.ForeignKey('Personne', on_delete=models.CASCADE, null=True, default=None, blank=True)
	idEtablissement = models.ForeignKey('Etablissement', on_delete=models.CASCADE, null=True, default=None, blank=True)
	idNiveau = models.ForeignKey('Niveau', on_delete=models.CASCADE, null=True, default=None, blank=True)
	idMessage = models.ForeignKey('Message', on_delete=models.CASCADE, null=False, blank=False)
	idVille = models.ForeignKey('Ville', on_delete=models.CASCADE, null=True, default=None, blank=True)
	def __str__(self):
		return 'statutEnvoi: ' + self.statutEnvoi

class MessageEnvoi(models.Model):
	aEnv = 'A envoyer'
	env = 'Envoyé'
	recu = 'Reçu'
	lu = 'Lu'
	envoi_choices = [
		(aEnv, 'A envoyer'),
		(env, 'Envoyé'),
		(recu, 'Reçu'),
		(lu, 'Lu')]
	statutEnvoi = models.CharField(max_length=50, choices=envoi_choices, default='A envoyer')
	#idEleve = models.ForeignKey('Eleve', on_delete=models.CASCADE, null=True)
	idPersonne = models.ForeignKey('Personne', on_delete=models.CASCADE, null=False)
	indicatif = models.CharField(null=True, default='228', max_length=4)
	texteMessage = models.TextField(max_length=6700)
	mobile = models.CharField(max_length=15, null=True)

	def __str__(self):
		return 'Ce message est pour: ' + str(self.idPersonne)