#Estrutura de Decisão Composta ("if-else")
#1. Questão 1: Maior ou Menor de Idade
#   - Enunciado: Escreva um programa que pergunte a idade do usuário e use a estrutura de decisão composta para imprimir
#   se ele é maior de idade ou não.

from datetime import date

#Entrada
an = int(input("Qual o ano do seu nascimento? "))
anoAtual = date.today().year

#processamento
idadeAtual = anoAtual - an
resposta = ""
if idadeAtual > 18:
    resposta = "Maior de idade"
else:
    resposta = "Menor de idade"

#Saída
print(resposta)
print("Você tem", idadeAtual, "anos")

