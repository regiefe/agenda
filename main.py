import os

class Agenda:
    def __init__(self, arquivo):
        self.contatos = open(arquivo,'r')
        self.contatos = self.contatos.readlines()

    def criar(self):
        os.system('clear')
        nome = input('Digite um nome: ')
        telefone = input('Digite um telefone: ')
        contato = nome+"; "+telefone+"\n"
        self.contatos.append(contato)
        self.contatos.sort()
        self._gravar('contatos.csv')

    def _gravar(self, arquivo):
        dados = open(arquivo, "w")
        tamanho =  len(self.contatos)

        for i in range(tamanho):
            dados.write(self.contatos[i])
        dados.close()

        print("Contato inserido com sucesso!")
        os.system("sleep 2s")

    def excluir(self):
        self.listar()
        delete = int(input("Qual deseja apagar? " ))
        self.contatos.pop(delete)
        print(f"Registro '{delete}' excluido")
        self._gravar('contatos.csv')
        os.system("sleep 1s")

    def listar(self):
        tamanho = len(self.contatos)

        for i in range(tamanho):
            print(i, "; ", self.contatos[i])

        os.system("sleep 1s")

agenda = Agenda('contatos.csv')
print(dir(agenda))

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
      agenda.criar()
   elif opcao ==  2:
       agenda.excluir()
   elif opcao ==  3:
       agenda.listar()
   elif opcao ==  4:
       break
   else:
       print('Opção invalida!')
       os.system("sleep 2s")