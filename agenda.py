import os

class Agenda:
    def __init__(self, arquivo):
        self.agenda = open(arquivo,'r')
        self.contatos = self.agenda.readlines()

    def criar(self):
        os.system('clear')
        nome = input('Digite um nome: ')
        telefone = input('Digite um telefone: ')
        contato = nome+"; "+telefone+"\n"
        self.contatos.append(contato)
        self.contatos.sort()
        self._gravar('contatos.csv')

    def _gravar(self, arquivo):
        agenda = open(arquivo, "w")
        tamanho =  len(self.contatos)

        for i in range(tamanho):
            agenda.write(self.contatos[i])
        agenda.close()

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

    def menu(self):
        os.system('clear')
        print('\n', "=" * 30)
        print("1 - Criar contato")
        print("2 - Excluir contato")
        print("3 - Listar contatos")
        print("4 - Sair")
        print('\n', "=" * 30)
        self.opcao =  int(input('Opcao: '))

    def start(self):
        while True:
           self.menu()
           if self.opcao ==  1:
              self.criar()
           elif self.opcao ==  2:
               self.excluir()
           elif self.opcao ==  3:
               self.listar()
           elif self.opcao ==  4:
               break
           else:
               print('Opção invalida!')
               os.system("sleep 2s")
