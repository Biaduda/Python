import random
nm1 = input('Digite o nome do primeiro aluno: ')
nm2 = input('Digite o nome do segundo aluno: ')
nm3 = input('Digite o nome do terceiro aluno: ')
nm4 = input('Digite o nome do quarto aluno: ')
lista = [nm1,nm2, nm3, nm4]
escolher=random.choice(lista)

print('O aluno escolhido foi {}'.format(escolher))