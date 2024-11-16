import random

# dicionario que armazena os produtos da loja
produtos = {
"fiat palio fire 2008": {"preço": 30.000, "estoque": 5},
"chevrolet astra 2011": {"preço": 35.000, "estoque": 7},
"ford escort wagon 1998": {"preço": 15.000, "estoque": 9},
"chevrolet montana": {"preço":27.900, "estoque": 5}

}







 # variavel que armazena o total de vendas realizasas 
total_vendas = 0.0

 # funçao para cadastrar um novo produtos
def exibir_produtos9():
    nome = "iput (digite o nome do produto: "
    preço = float(input(f"digite o preço de (nome)"))
    
    estoque = float(input(f"digite a quantida de estoque de {nome}: "))
produtos[nome] = {"preço": proco, "estoque": estoque}
print(f"produto [nome] cadastrado com sucesso!`\n")
 
 # funçao para exibir os produtos disponiveis
def exibir_produtos():
    print("\nprodutos disponiveis:")
    for produto, info in produtos.items():
        print(f"{produto} - preço: r${info['preço']:.2f}, estoque: {info['estoque']}")
        print()

        #funçao para realizar essa venda
        def realizar_venda():
            global total_vendas
            produto_vendido = input("digite o nome do produto que deseja")

            # verifica se o produto existe e se ha estoque
            if produto_vendido in produtos:
                quantidade = int(input(f"digite a quantidade de (produtos_vendido) que deseja compear"))
                if produtos{produto_vendido}{"estoque"} >= quantidade:
                    valor_venda += valor_venda   
 print(venda realizada: quantidade)x {produto_vendido}- total: r${valor_venda:.2f}\n"
else:
print("quantidade em estoque insuficiente para venda.\n")
else:
print("produto nao encontrado") 
  #funçao para aplicar uma promoçao 
def sortear_promoçao():
    produto_sorteado = random.choice(list(produtos.keys()))
    desconto = random.randint(10,50) #desconto entre 10% e 50%
    produtos[produto_sorteado]["preço"]*= (1 - desconto/100)
    print(f"\npromoçao: o produto {produto_sorteado}esta com {desconto}$ de desconto)% de desconto!\n")

    # menu pricipal
def menu ()
while true:
            print("=== sistema de gerenciamento de loja ===")
            print("1. cadastrar produto")
            print("2. exibir produtos")
            print("3. realizar venda ")
            print("4.exibir total de vendas")
            print("5,sortear promoçao")
            print("6. sair")

            opçao = input("escolha uma opçao")

            if opçao == "1":
                cadastrar_produto()
         elif opçao == "2":
                 exibir_produtos()
          elif opçao == "3":
            realizar_vendas()  
            elif opçao == "4":
                exibir_vendas()
                elif opçao =="5":
                    sortear_promoçao()
                elif opcao == "6":
                print("saindo do sistema...")
                break
            else:
                print("opçao invalidade: tente novamente.\n")
                # iniciar o sistema
                menu()


                    
    

