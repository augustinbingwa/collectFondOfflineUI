from django.utils import timezone
from django.contrib.auth.models import User
from random import choice, randint
from string import ascii_letters, digits
from apps.home.models import Client,Cotisation
from apps.home.enums import *

import django
from core import settings

django.setup()

# Génération aléatoire de noms et prénoms
noms = ['Dupont', 'Martin', 'Durand', 'Dubois', 'Leblanc']
prenoms = ['Alice', 'Bob', 'Charles', 'David', 'Emma']


# Génération aléatoire de codes clients
def generate_code_cotisation():
    chars = digits
    annee = timezone.now().year
    mois = timezone.now().month
    return f'TRS{annee}{mois}' + ''.join(choice(chars) for _ in range(6))


# Récupération d'un utilisateur existant pour la clé étrangère 'util_cree'
utilisateur = User.objects.first()
client = Client.objects.all()

# Création des cotisations
for i in client:
    code_transaction = generate_code_cotisation()
    code_client = i.code_client
    montant = f'{randint(6 ** 3, 6 ** 3)}000'
    date_cotisation = timezone.now()
    type_cotisation = choice([c[0] for c in choix_type_cotisation])
    periode_cotisation = choice([c[0] for c in choix_periode_cotisation])
    paiement_effectue = True
    util_cree = utilisateur

    # Création de l'objet Cotisation et enregistrement en base de données
    cotisation = Cotisation.objects.create(
        code_transaction=code_transaction,
        code_client=code_client,
        montant=montant,
        date_cotisation=date_cotisation,
        type_cotisation=type_cotisation,
        periode_cotisation=periode_cotisation,
        paiement_effectue=paiement_effectue,
        util_cree=util_cree
    )
    cotisation.save()