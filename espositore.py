
class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice # proteggo/nascondo l'accesso agli attributi con __
        self.__nome = nome
        self.__cognome = cognome
        self.__stand_assegnato = None

    # solo in lettura perchè non devono essere modificati
    @property
    def codice(self):
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @ property
    def cognome(self):
        return self.__cognome

    # lettura + modifica perchè lo stand assegnato può cambiare
    @property
    def stand_assegnato(self):
        return self.__stand_assegnato
    @stand_assegnato.setter
    def stand_assegnato(self, stand):
        self.__stand_assegnato = stand

    # per confrontare due oggetti tramite l'operatore ==
    # permette di stabilire quando due istanze devono essere considerate uguali
    def __eq__(self,other):
        if isinstance(other, Espositore):
            # due espositori sono uguali se hanno lo stesso codice
            return self.__codice == other.__codice
        else:
            return False

    # definiamo la stampa per ESPOSITORE
    def __str__(self):
        if self.__stand_assegnato is not None:
            stand_assegnato = f"Stand: {self.__stand_assegnato.codice}"
        else:
            stand_assegnato = "Nessuno stand assegnato"

        return f"Espositore: {self.__codice}: {self.__nome} {self.__cognome} - {stand_assegnato}"