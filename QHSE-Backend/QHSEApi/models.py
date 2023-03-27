from django.db import models

from django.db import models

#modèle de la classe commande 

class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.DateTimeField()
    type_commande = models.CharField(max_length=50)
    etat_commande = models.CharField(max_length=50)
    quantite = models.IntegerField()
    specificite_regime = models.CharField(max_length=50)
    specificite_texture = models.CharField(max_length=50)
    type_auth = models.CharField(max_length=50)
    def __str__(self):
        return f"Commande {self.id_commande} du {self.date_commande}"

#modèle de la classe Fiche Technique 
class FicheTechnique(models.Model):
    id_fiche = models.AutoField(primary_key=True)
    url_fiche = models.CharField(max_length=255)
    nom_fiche = models.CharField(max_length=255)
    type_plat = models.CharField(max_length=50)

#modèle de la classe Document

class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    nom_document = models.CharField(max_length=255)
    codification = models.CharField(max_length=50, null=True, blank=True)
    version = models.IntegerField()
    date_approbation = models.DateField()
    date_previsionnelle = models.DateField(null=True, blank=True)
    nouvelle_version = models.BooleanField()
    type_document = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id_document} - {self.nom_document} - {self.version}"
    
#modèle de la classe Historique_Document
class HistoriqueDocument(models.Model):
    id_historique = models.AutoField(primary_key=True)
    id_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    version = models.CharField(max_length=10)
    modifie_par = models.ForeignKey(User, on_delete=models.CASCADE)
    description_modification = models.TextField()
    

    def __str__(self):
        return f"{self.id_historique} - {self.id_document} - {self.version} - {self.modifie_par}"

#modèle de la classe Favoris_Document