from rest_framework import serializers
from .models import FicheTechnique
from .models import Commande
#Serializer pour la fiche technique 
class FicheTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTechnique
        fields = ('id_fiche', 'url_fiche', 'nom_fiche', 'type_plat')

#Serializer pour la commande
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('id_commande', 'date_commande', 'type_commande', 'etat_commande', 'quantite', 'specificite_regime', 'specificite_texture', 'type_auth')
