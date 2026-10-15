
class Stand:
    def __init__(self, codice, metri_quadri, padiglione, prezzo_base):
        # proteggo/nascondo l'accesso agli attributi con __
        self.__codice = codice
        self.__metri_quadri = metri_quadri
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base
        self.__espositore = None # espositore assegnato

    @property
    def codice(self):
        return self.__codice

    @property
    def metri_quadri(self):
        return self.__metri_quadri

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

    # per lo stand STANDARD il prezzo rimane quello base
    def calcola_prezzo(self):
        return self.__prezzo_base

    # per confrontare due Stand con l'operatore ==
    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.__codice == other.codice
        else:
            return False

    # permette di stabilire quando un oggetto è minore( <) di un altro
    # confronto per poter ordinare la lista per prezzo
    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        else:
            return False

    # stampa per lo STAND
    def __str__(self):
        # verifica disponibilità degli stand
        if self.__espositore is None:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.__espositore.codice}"

        return f"{self.__codice}: Standard | {self.__metri_quadri} mq - Padiglione {self.__padiglione}- Prezzo {self.calcola_prezzo():.2f}€ - {stato}"