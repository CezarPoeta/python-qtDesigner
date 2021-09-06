class Bascara_1():
    def __init__(self, pvalor):
        self.atr_valor = pvalor
        msg='Entrou na Bascara_1'
        return print(msg)


    def calc_bas(self):
        val = self.atr_valor * 2
        return val

    #Getter
    @property
    def atr_valor(self):
        return self._atr_valor

    #Setter - O uso do Getter/Setter possibilita consistir, validar os atributos passados para a Classe.
    @atr_valor.setter
    def atr_valor(self, pvalor):
        if isinstance(pvalor, str):
            pvalor = float(pvalor.replace('R$',''))

        self._atr_valor = pvalor



