from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from QHSEApi.models import Commande, FicheTechnique

from QHSEApi.serializer import CommandeSerializer, FicheTechniqueSerializer
from django.core.files.storage import default_storage

# CRUD pour les commandes

@csrf_exempt
def commandeApi(request, id=0):
    if request.method== 'GET':
        commandes= Commande.objects.all()
        commandeSerializer = CommandeSerializer(commandes,many=True)
        return JsonResponse(commandeSerializer.data, safe=False)
    elif request.method=='POST':
        commande_data= JSONParser().parse(request)
        commandeSerializer= CommandeSerializer(data=commande_data)
        if commandeSerializer.is_valid():
            commandeSerializer.save()
            return JsonResponse('Added successfully ', safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        commande_data = JSONParser().parse(request)
        commande = Commande.objects.get(id_commande=commande_data['id_commande'])
        commandeSerializer = CommandeSerializer(commande, data=commande_data)
        if commandeSerializer.is_valid():
            commandeSerializer.save()
            return JsonResponse('Update successfully ', safe=False)
        return JsonResponse('Failed to update', status=400)
    
    elif request.method=='DELETE':
        commande= Commande.objects.get(id_commande=id)
        commande.delete()
        return JsonResponse('Deleted successfully', safe=False)


# CRUD pour les fiches techniques
@csrf_exempt
def FicheApi(request, id=0):
    if request.method == 'GET':
        fiches = FicheTechnique.objects.all()
        
        ficheSerializer = FicheTechniqueSerializer(fiches, many=True)
        return JsonResponse(ficheSerializer.data, safe=False)
    
    elif request.method == 'POST':
        fiche_data = JSONParser().parse(request)
        ficheSerializer = FicheTechniqueSerializer(data=fiche_data)
        if ficheSerializer.is_valid():
            ficheSerializer.save()
            return JsonResponse('Added successfully ', safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        fiche_data = JSONParser().parse(request)
        fiche = FicheTechnique.objects.get(id_fiche=fiche_data['id_fiche'])
        ficheSerializer = FicheTechniqueSerializer(fiche, data=fiche_data)
        if ficheSerializer.is_valid():
            ficheSerializer.save()
            return JsonResponse('Update successfully ', safe=False)
        return JsonResponse('Failed to update', status=400)
    
    elif request.method == 'DELETE':
        fiche = FicheTechnique.objects.get(id_fiche=id)
        fiche.delete()
        return JsonResponse('Deleted successfully', safe=False)
    
   
