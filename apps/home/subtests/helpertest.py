import datetime
from django.test import TestCase
from home.helpers import generate_serial_number

generate_serial_number.last_month = datetime.date.today().month

class TestGenerateSerialNumber(TestCase):
    def test_serial_number_format(self):
        # Vérifie que le format du numéro de série est correct
        serial_number = generate_serial_number()
        self.assertRegex(serial_number, r"SN\d{6}-\d{4}")

    def test_monthly_reset(self):
        # Vérifie que le compteur est réinitialisé chaque début de mois
        today = datetime.date.today()
        expected_counter = 0
        # Appeler la fonction plusieurs fois pour s'assurer que le compteur est incrémenté correctement
        for _ in range(10):
            if today.month != generate_serial_number.last_month:
                expected_counter = 1
                generate_serial_number.last_month = today.month
            else:
                expected_counter += 1
            serial_number = generate_serial_number()
            self.assertEqual(serial_number[-4:], f"{expected_counter:05}")
