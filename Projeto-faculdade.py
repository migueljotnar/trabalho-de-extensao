import csv
import os

# Nome do arquivo CSV
arquivo_estoque = 'estoque.csv'
# Função para inicializar o arquivo de estoque (caso não exista)
def inicializar_estoque():
    if not os.path.exists(arquivo_estoque):
        with open(arquivo_estoque, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Preço', 'Quantidade'])  # Cabeçalhos
        print('Arquivo de estoque criado.')

# Função para adicionar um novo produto ao estoque
def adicionar_produto(nome, preco, quantidade):
    with open(arquivo_estoque, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, preco, quantidade])
    print(f'Produto {nome} adicionado com sucesso.')

# Função para listar todos os produtos
def listar_produtos():
    with open(arquivo_estoque, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula os cabeçalhos
        produtos = list(reader)
        if not produtos:
            print("Nenhum produto encontrado.")
        else:
            print("Nome | Preço | Quantidade")
            for produto in produtos:
                print(f'{produto[0]} | R${produto[1]} | {produto[2]} unidades')

# Função para atualizar o estoque de um produto
def atualizar_estoque(nome_produto, quantidade_vendida):
    produtos_atualizados = []
    estoque_atualizado = False

    with open(arquivo_estoque, mode='r') as file:
        reader = csv.reader(file)
        produtos = list(reader)

    for produto in produtos:
        if produto[0] == nome_produto:
            quantidade_nova = int(produto[2]) - quantidade_vendida
            if quantidade_nova < 0:
                print(f'Estoque insuficiente para o produto {nome_produto}.')
                return
            produto[2] = str(quantidade_nova)
            estoque_atualizado = True
        produtos_atualizados.append(produto)

    if estoque_atualizado:
        with open(arquivo_estoque, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(produtos_atualizados)
        print(f'Estoque do produto {nome_produto} atualizado com sucesso.')
    else:
        print(f'Produto {nome_produto} não encontrado no estoque.')

# Função para alertar produtos com estoque baixo
def alerta_estoque_baixo(limite):
    with open(arquivo_estoque, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula os cabeçalhos
        produtos = list(reader)
        estoque_baixo = [produto for produto in produtos if int(produto[2]) <= limite]

    if estoque_baixo:
        print("Produtos com estoque baixo:")
        for produto in estoque_baixo:
            print(f'{produto[0]} - {produto[2]} unidades restantes')
    else:
        print("Nenhum produto com estoque baixo.")

# Função principal para testar o sistema
if __name__ == '__main__':
    inicializar_estoque()

    adicionar_produto('Arroz', 20.50, 50)
    adicionar_produto('Feijão', 8.30, 30)
    adicionar_produto('Óleo', 7.10, 15)

    listar_produtos()

    atualizar_estoque('Feijão', 5)

    listar_produtos()

    alerta_estoque_baixo(10)
