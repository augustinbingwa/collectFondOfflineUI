from django.utils import timezone
from django.contrib.auth.models import User
from random import choice, randint
from string import ascii_letters, digits
from apps.home.models import Client
from apps.home.enums import *

import django
from core import settings

django.setup()

# Génération aléatoire de noms et prénoms
noms = ['Dupont', 'Martin', 'Durand', 'Dubois', 'Leblanc']
prenoms = ['Alice', 'Bob', 'Charles', 'David', 'Emma']


# Génération aléatoire de codes clients
def generate_code_client():
    chars = ascii_letters + digits
    return ''.join(choice(chars) for _ in range(10))


# Récupération d'un utilisateur existant pour la clé étrangère 'util_cree'
utilisateur = User.objects.first()

# Création des 50 clients
for i in range(100):
    nom = choice(noms)
    prenom = choice(prenoms)
    numero_carte = f'ABCD{randint(1000, 9999)}' if i % 3 == 0 else None
    genre = choice([c[0] for c in choix_genre])
    email = f'{prenom.lower()}.{nom.lower()}@example.com'
    telephone = f'06{randint(10 ** 8, 10 ** 9 - 1)}'
    code_client = generate_code_client()
    date_creation = timezone.now()

    # Création de l'objet Client et enregistrement en base de données
    client = Client.objects.create(nom=nom, prenom=prenom, numero_carte=numero_carte, genre=genre, email=email,
                                   telephone=telephone, code_client=code_client, date_creation=date_creation,
                                   util_cree=utilisateur)
    client.save()
