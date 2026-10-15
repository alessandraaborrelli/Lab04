from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, metri_quadri, padiglione, prezzo_base, posizione):
        super().__init__(codice, metri_quadri, padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    # calcola prezzo con maggiorazione del 30%
    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    # stampa per lo STAND PREMIUM
    def __str__(self):
        if self.espositore is None:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.espositore.codice}"

        return f"{self.codice}: Premium | {self.metri_quadri} mq - Padiglione {self.padiglione}- Prezzo {self.calcola_prezzo():.2f}€ - Posizione: {self.__posizione} - {stato}"