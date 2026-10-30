
import unittest
from paiements import Paiement, CarteBancaire, PayPal, Crypto


class TestPaiements(unittest.TestCase):

    def test_carte(self):
        p = CarteBancaire(100, "4111111111111111", "123")
        self.assertIn("100", p.payer())
        self.assertIn("Carte Bancaire", p.payer())

    def test_paypal(self):
        p = PayPal(200, "test@gmail.com", "token123")
        self.assertIn("200", p.payer())
        self.assertIn("PayPal", p.payer())

    def test_crypto(self):
        p = Crypto(300, "wallet123", "BTC")
        self.assertIn("300", p.payer())
        self.assertIn("Crypto", p.payer())

    def test_montant_negatif(self):
        with self.assertRaises(ValueError):
            PayPal(-100, "test@gmail.com", "token123")

    def test_carte_invalide(self):
        with self.assertRaises(ValueError):
            CarteBancaire(100, "1234567890123456", "123")

    def test_classe_abstraite(self):
        with self.assertRaises(TypeError):
            Paiement(100)


if __name__ == "__main__":
    unittest.main()
