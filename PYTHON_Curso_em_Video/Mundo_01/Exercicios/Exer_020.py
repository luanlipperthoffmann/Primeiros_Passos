'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
aluno1 = input("Dígite o nome do 1º aluno: ")
aluno2 = input("Dígite o nome do 2º aluno: ")
aluno3 = input("Dígite o nome do 3º aluno: ")
aluno4 = input("Dígite o nome do 4º aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f"A ordem dos alunos escolidos foi: {lista}")