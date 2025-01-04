import random


class Produto:
    def __init__(self, nome, secao):
        self._nome = nome
        self._secao = secao
        self._preco = self.gerar_preco_aleatorio()


    
    @property
    def nome(self):
        return self._nome

    @property
    def secao(self):
        return self._secao

    @property
    def preco(self):
        return self._preco

    # Método para gerar um preço aleatório dentro do intervalo da seção
    def gerar_preco_aleatorio(self):
        preco_minimo, preco_maximo = self.secao.obter_intervalo_preco()
        return random.randint(preco_minimo, preco_maximo)
    