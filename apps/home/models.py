from django.db import models
from django.conf import settings
from .enums import *
# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_carte = models.CharField(max_length=100,null=True)
    genre = models.IntegerField(choices=choix_genre,default=FEMME)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=20)
    code_client = models.CharField(max_length=10,null=True,db_index=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    util_cree = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='%(class)s_requests_util_cree')

class Cotisation(models.Model):
    code_transaction = models.CharField(max_length=20, null=True)
    code_client = models.CharField(max_length=10,db_index=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_cotisation = models.DateField(db_index=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)
    paiement_effectue = models.BooleanField(default=False)
    type_cotisation = models.IntegerField(choices=choix_type_cotisation,default=JOURNALIER,db_index=True)
    periode_cotisation = models.IntegerField(choices=choix_periode_cotisation,null=True,db_index=True)
    util_cree = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='%(class)s_requests_util_cree')
    util_modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='%(class)s_requests_util_modifier', null=True)

class Rapport(models.Model):
    date = models.DateField()
    total_cotisations = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_cotisations = models.IntegerField()
    nombre_client_cotise = models.IntegerField()
    nombre_collecteur = models.IntegerField()

