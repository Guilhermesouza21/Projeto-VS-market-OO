class Carrinho:
    def __init__(self):
        self._produtos = []  # Lista para armazenar os produtos no carrinho

    def adicionar_produto(self, produto):
        self._produtos.append(produto)

    def remover_produto(self, nome_produto):
        for produto in self._produtos:
            if produto.nome == nome_produto:
                self._produtos.remove(produto)
                return produto
        return None

    def calcular_total(self):
        return sum(produto.preco for produto in self._produtos)

    def exibir_produtos(self):
        if not self._produtos:
            print("O carrinho está vazio.")
            return
        for produto in self._produtos:
            print(f"Produto: {produto.nome}, Preço: {produto.preco}")


    def finalizar_compra(self):
        total = self.calcular_total()
        if total == 0:
            print("Carrinho vazio! Não é possível realizar o pagamento.")
            return False
        return True
    
#teste github


    
      