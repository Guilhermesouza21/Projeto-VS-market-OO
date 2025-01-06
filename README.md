# Projeto-VS-market-OO

# VS Market - Sistema de Compras Simulado

Bem-vindo ao **VS Market**, um sistema de compras simulado que permite a interação de clientes com seções, carrinhos de compras e produtos. Este projeto foi desenvolvido para demonstrar conceitos de programação orientada a objetos em Python.

---

## Funcionalidades

- **Carrinho de Compras**:
  - Adicionar e remover produtos.
  - Calcular o total do carrinho.
  - Finalizar compras com histórico salvo em um arquivo JSON.

- **Gestão de Seções**:
  - Seções categorizadas com intervalos de preço específicos.
  - Pesquisa e adição de produtos por seção.

- **Produtos**:
  - Cada produto possui um nome e um preço gerado aleatoriamente dentro do intervalo de preços definido pela seção correspondente.

- **Cliente**:
  - Interação com o carrinho.
  - Histórico de compras salvo em JSON.

---

## Estrutura do Projeto

- `Carrinho.py`: Implementa a lógica para o carrinho de compras.
- `Client.py`: Contém a classe `Cliente` e gerencia as interações principais.
- `Seção.py`: Define as seções disponíveis para compra e os intervalos de preços.
- `main.py`: Arquivo principal para executar o sistema.
- `Produto.py`:Objeto que tem valores aleatorios ao ser pesquisado.
---

## Pré-requisitos

- Python 3.8 ou superior.

---

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>

---

## Como Usar o Sistema

Depois de executar o código com o comando:

```bash
python main.py


Escolher seção:

O sistema exibirá uma lista de seções disponíveis, como "Eletrônicos", "Livros", etc.
Você deve selecionar uma seção digitando o número correspondente.
Após escolher, poderá pesquisar produtos dentro dessa seção.
Interagir com o carrinho:

Permite gerenciar os produtos no carrinho com as seguintes opções:
Ver os produtos adicionados ao carrinho.
Remover produtos pelo nome.
Ver o total acumulado no carrinho.
Finalizar a compra e salvar o histórico.
Sair:

Encerra o sistema e retorna ao terminal.

