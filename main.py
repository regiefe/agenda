#!/usr/bin/env python

from agenda import Agenda
import os

agenda = Agenda('contatos.csv')
print(dir(agenda))


while True:
   opcao = agenda.menu()
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
