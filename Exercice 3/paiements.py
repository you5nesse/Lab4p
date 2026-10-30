
from abc import ABC, abstractmethod


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self._numero = str(numero)
        self._cvv = str(cvv)

        if not self.verifier_carte():
            raise ValueError("Numéro de carte invalide")

        if not (self._cvv.isdigit() and len(self._cvv) in (3, 4)):
            raise ValueError("CVV invalide")

    def verifier_carte(self):
        if not self._numero.isdigit():
            return False

        if not 13 <= len(self._numero) <= 19:
            return False

        total = 0

        for i, chiffre in enumerate(reversed(self._numero)):
            n = int(chiffre)

            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9

            total += n

        return total % 10 == 0

    def payer(self):
        return f"Carte Bancaire : paiement de {self._montant} DH confirmé"


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self._email = email
        self._token = token

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email invalide")

        if not token:
            raise ValueError("Token invalide")

    def payer(self):
        return f"PayPal : paiement de {self._montant} DH confirmé"


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

        if not wallet_id:
            raise ValueError("Wallet invalide")

        if reseau not in ("BTC", "ETH"):
            raise ValueError("Réseau non supporté")

    def payer(self):
        return f"Crypto ({self._reseau}) : paiement de {self._montant} DH confirmé"


def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


if __name__ == "__main__":
    paiements = [
        CarteBancaire(150, "4111111111111111", "123"),
        CarteBancaire(250, "5555555555554444", "456"),
        PayPal(300, "alice@gmail.com", "token123"),
        PayPal(450, "bob@gmail.com", "token456"),
        Crypto(500, "wallet001", "BTC"),
        Crypto(700, "wallet002", "ETH")
    ]

    traiter_paiements(paiements)
