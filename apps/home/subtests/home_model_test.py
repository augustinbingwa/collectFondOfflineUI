from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from home.models import Client,Cotisation,Rapport
from home.enums import *
from django.utils import timezone

class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        Client.objects.create(
            nom='Doe',
            prenom='John',
            genre=FEMME,
            email='johndoe@example.com',
            telephone='1234567890',
            util_cree=user
        )

    def test_client_creation(self):
        client = Client.objects.get(id=1)
        self.assertEqual(client.nom, 'Doe')
        self.assertEqual(client.prenom, 'John')
        self.assertEqual(client.genre, FEMME)
        self.assertEqual(client.email, 'johndoe@example.com')
        self.assertEqual(client.telephone, '1234567890')
        self.assertEqual(client.util_cree.username, 'testuser')

    def test_client_str(self):
        client = Client.objects.get(id=1)
        self.assertEqual(str(client), 'Doe John')

class CotisationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cotisation = Cotisation.objects.create(
            code_transaction='ABCD1234',
            code_client='1234567890',
            montant=100.0,
            date_cotisation='2022-03-18',
            paiement_effectue=False,
            type_cotisation=1,
            periode_cotisation=1,
            util_cree=self.user,
        )

    def test_cotisation_creation(self):
        self.assertTrue(isinstance(self.cotisation, Cotisation))
        self.assertEqual(self.cotisation.__str__(), self.cotisation.code_transaction)
        self.assertEqual(self.cotisation.code_client, '1234567890')
        self.assertEqual(self.cotisation.montant, 100.0)
        self.assertEqual(self.cotisation.date_cotisation, '2022-03-18')
        self.assertFalse(self.cotisation.paiement_effectue)
        self.assertEqual(self.cotisation.type_cotisation, 1)
        self.assertEqual(self.cotisation.periode_cotisation, 1)
        self.assertEqual(self.cotisation.util_cree, self.user)

    def test_cotisation_update(self):
        self.cotisation.code_client = '0987654321'
        self.cotisation.save()
        updated_cotisation = Cotisation.objects.get(id=self.cotisation.id)
        self.assertEqual(updated_cotisation.code_client, '0987654321')

class RapportModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.rapport = Rapport.objects.create(
            date=timezone.now().date(),
            total_cotisations=100.00,
            nombre_cotisations=5,
            nombre_client_cotise=3,
            nombre_collecteur=2,
            util_cree=self.user,
        )

    def test_rapport_creation(self):
        rapport = self.rapport
        self.assertTrue(isinstance(rapport, Rapport))
        self.assertEqual(str(rapport), rapport.date.strftime('%d/%m/%Y'))
        self.assertEqual(rapport.total_cotisations, 100.00)
        self.assertEqual(rapport.nombre_cotisations, 5)
        self.assertEqual(rapport.nombre_client_cotise, 3)
        self.assertEqual(rapport.nombre_collecteur, 2)
        self.assertEqual(rapport.util_cree, self.user)
        self.assertEqual(str(rapport.date), timezone.now().date().strftime('%Y-%m-%d'))
