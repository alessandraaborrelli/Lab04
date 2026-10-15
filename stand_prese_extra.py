from stand import Stand

# classe figlia, la quale eredita tutti gli attributi della classe padre tramite super().
class StandPreseExtra(Stand):
    def __init__(self, codice, metri_quadri, padiglione, prezzo_base, prese_extra):
        super().__init__(codice, metri_quadri, padiglione, prezzo_base)
        self.__prese_extra = prese_extra # numero di prese extra disponibili

    @property
    def prese_extra(self):
        return self.__prese_extra

    # calcolo del sovrapprezzo pari al 7% per ogni presa extra
    # sovrascrive calcola_prezzo()
    def calcola_prezzo(self):
        fattore = 1 + (0.07 * self.__prese_extra)
        return self.prezzo_base * fattore

    # stampa per STAND con PRESE EXTRA
    def __str__(self):
        if self.espositore is None:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.espositore.codice}"

        return f"{self.codice}: Prese Extra | {self.metri_quadri} mq - Padiglione {self.padiglione}- Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.__prese_extra} - {stato}"