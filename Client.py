import json
from Produto import Produto
from Carrinho import Carrinho
from Seção import secoes_disponiveis

class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._carrinho = Carrinho()

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def carrinho(self):
        return self._carrinho

    def salvar_historico(self, arquivo="historico_compras.json"):
        historico = {
            "cliente": self.nome,
            "idade": self.idade,
            "compras": [{
                "nome_produto": produto.nome,
                "preco": produto.preco,
                "secao": produto.secao.nome
            } for produto in self.carrinho._produtos],
            "total": self.carrinho.calcular_total()
        }

        try:
            with open(arquivo, 'r') as f:
                dados_existentes = json.load(f)
        except FileNotFoundError:
            dados_existentes = []

        dados_existentes.append(historico)

        with open(arquivo, 'w') as f:
            json.dump(dados_existentes, f, indent=4)
        print("Histórico de compras salvo com sucesso!")

    def finalizar_compra(self):
        if self.carrinho.finalizar_compra():
            total = self.carrinho.calcular_total()
            print(f"Compra finalizada! Total: R${total}")
            self.salvar_historico()
            self._carrinho = Carrinho()  # Limpa o carrinho para novas compras

    def escolher_secao(self, secoes):
        while True:
            print("\nEscolha uma seção:")
            for i, secao in enumerate(secoes):
                print(f"{i + 1}. {secao.nome}")
            
            try:
                escolha = int(input("Digite o número da seção desejada: ")) - 1
                if 0 <= escolha < len(secoes):
                    return secoes[escolha]
                else:
                    print("Escolha inválida! Por favor, digite um número válido da lista.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

    def pesquisar_produto(self, secao):
        while True:
            nome_produto = input(f"\nDigite o nome do produto que deseja buscar na seção {secao.nome} (ou digite 'sair' para voltar): ")
            if nome_produto.lower() == 'sair':
                break
            produto = Produto(nome_produto, secao)
            print(f"Produto encontrado: {produto.nome} - Preço: {produto.preco}")
            adicionar = input("Deseja adicionar este produto ao carrinho? (s/n): ")
            if adicionar.lower() == 's':
                self.carrinho.adicionar_produto(produto)
                print(f"{produto.nome} adicionado ao carrinho.")

    def interagir_com_carrinho(self):
        while True:
            print("\nO que você deseja fazer com o carrinho?")
            print("1. Ver produtos no carrinho")
            print("2. Remover um produto")
            print("3. Ver total do carrinho")
            print("4. Finalizar compra")
            print("5. Voltar ao menu principal")
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    self.carrinho.exibir_produtos()
                elif escolha == 2:
                    nome_produto = input("Digite o nome do produto a ser removido: ")
                    produto_removido = self.carrinho.remover_produto(nome_produto)
                    if produto_removido:
                        print(f"{produto_removido.nome} removido do carrinho.")
                    else:
                        print("Produto não encontrado no carrinho.")
                elif escolha == 3:
                    total = self.carrinho.calcular_total()
                    print(f"Total do carrinho: R${total}")
                elif escolha == 4:
                    self.finalizar_compra()
                    break
                elif escolha == 5:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

# Criando um cliente e interagindo com o sistema
cliente = Cliente("João", 30)

print("Bem-vindo ao VS Market! Seu destino para as melhores compras!")
print(f"Olá, {cliente.nome}! Estamos felizes em tê-lo conosco.\n")

while True:
    print("\nMenu Principal:")
    print("1. Escolher seção")
    print("2. Interagir com o carrinho")
    print("3. Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            secao_escolhida = cliente.escolher_secao(secoes_disponiveis)
            cliente.pesquisar_produto(secao_escolhida)
        elif opcao == 2:
            cliente.interagir_com_carrinho()
        elif opcao == 3:
            print("Obrigado por usar nosso sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")
