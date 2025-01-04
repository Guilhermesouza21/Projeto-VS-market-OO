# Classe Secao
class Secao:
    #precos minimos e maximos
    def __init__(self, nome, preco_minimo, preco_maximo):
        self.nome = nome
        self.preco_minimo = preco_minimo
        self.preco_maximo = preco_maximo

    # Método para obter o intervalo de preços da seção
    def obter_intervalo_preco(self):
        return self.preco_minimo, self.preco_maximo
    


secoes_disponiveis = [
    Secao("Eletrônicos", 100, 1000),
    Secao("Móveis", 400, 3000),
    Secao("Eletrodomésticos", 200, 2000),
    Secao("Livros", 20, 500),
    Secao("Roupas", 20, 100),
    Secao("Esportes", 100, 2000),
    Secao("Brinquedos", 30, 800)
]