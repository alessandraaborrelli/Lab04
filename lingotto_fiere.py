import csv
from stand import Stand
from espositore import Espositore
from stand_premium import StandPremium
from stand_prese_extra import StandPreseExtra

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.stand = {} # dizionario per salvare gli stand
        self.espositori = {}

    """Aggiungere setter e getter se necessari"""
    # TODO
    # per modificare il nome del centro fieristico
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            filein = open(file_path,'r')
            file_read = csv.reader(filein)
            for riga in file_read:
                codice = riga[0]

                if codice.startswith("ST"):
                    metri_quadri = float(riga[1].strip())
                    padiglione = int(riga[2].strip())
                    prezzo_base = float(riga[3].strip())

                    # se ci sono solo 4 colonne
                    if len(riga) == 4:
                        nuovo_stand = Stand(codice,metri_quadri, padiglione, prezzo_base)
                        self.stand[codice] = nuovo_stand

                    # se c'è un quinto valore
                    elif len(riga) >= 5:
                        valore_extra = riga[4].strip()
                        # isdigit ritorna True se il valore contiene solo cifre numeriche
                        # ritorna False se contiene caratteri
                        if valore_extra.isdigit():
                            nuovo_stand = StandPreseExtra(codice, metri_quadri, padiglione, prezzo_base, int(valore_extra))
                            self.stand[codice] = nuovo_stand
                        else:
                            nuovo_stand = StandPremium(codice, metri_quadri, padiglione, prezzo_base, valore_extra)
                            self.stand[codice] = nuovo_stand

                elif codice.startswith("ES"):
                    nome = riga[1].strip()
                    cognome = riga[2].strip()
                    espositore = Espositore(codice, nome, cognome)
                    self.espositori[codice] = espositore
        except FileNotFoundError:
            print("File non trovato!")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        if codice_stand not in self.stand:
            raise KeyError(f"Lo stand {codice_stand} non esiste")
        if codice_espositore not in self.espositori:
            raise KeyError(f"L'espositore {codice_espositore} non esiste")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]

        if stand.espositore is not None:
            raise Exception(f"Lo stand {codice_stand} è occupato")
        elif espositore.stand_assegnato is not None:
            raise Exception(f"L'espositore {codice_espositore} ha già uno stand assegnato")
        else:
            stand.espositore = espositore
            espositore.stand_assegnato = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        if len(self.espositori) == 0:
            print("Nessun espositore presente")
        else:
            for espositore in self.espositori.values():
                print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        lista_stand = list(self.stand.values())
        return sorted(lista_stand)
