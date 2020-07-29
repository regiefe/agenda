import os

contatos = []
arquivo = open('contatos.csv','r')
contatos = arquivo.readlines()
arquivo.close()

def criar(contatos):
    os.system('clear')
    nome = input('Digite um nome: ')
    telefone = input('Digite um telefone: ')
    contato = nome+"; "+telefone+"\n"
    contatos.append(contato)
    contatos.sort()
    gravar(contatos)

def gravar(contatos):
    arquivo = open("contatos.csv", "w")
    tamanho =  len(contatos)

    for i in range(tamanho):
        arquivo.write(contatos[i])
    arquivo.close()

    print("Contato inserido com sucesso!")
    os.system("sleep 2s")

def excluir(contatos):
    listar(contatos)
    delete = int(input("Qual deseja apagar? " ))
    contatos.pop(delete)
    print(f"Registro '{delete}' excluido")
    gravar(contatos)
    os.system("sleep 1s")

def listar(contatos):
    tamanho = len(contatos)

    for i in range(tamanho):
        print(i, "; ", contatos[i])

    os.system("sleep 1s")

def menu():
    os.system('clear')
    print('\n', "=" * 30)
    print("1 - Criar contato")
    print("2 - Excluir contato")
    print("3 - Listar contatos")
    print("4 - Sair")
    print('\n', "=" * 30)
    opcao =  input('Opcao: ')
    return int(opcao)

while True:
   opcao = menu()
   if opcao ==  1:
       criar(contatos)
   elif opcao ==  2:
       excluir(contatos)
   elif opcao ==  3:
       listar(contatos)
   elif opcao ==  4:
       break
   else:
       print('Opção invalida!')
       os.system("sleep 2s")
