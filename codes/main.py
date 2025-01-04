# Importando diretamente os módulos
from Client import Cliente
from Seção import secoes_disponiveis

def main():
    # Criar um cliente
    cliente = Cliente("João", 30)
    print(f"Bem-vindo ao VS Market, {cliente.nome}!")

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

if __name__ == "__main__":
    main()
