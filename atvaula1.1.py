#1. Questão 1: Verificar Positividade
#- Enunciado: Escreva um programa que peça ao usuário para digitar um número. Use a estrutura de decisão simples para verificar se o número é positivo. Se for, imprima "O número é positivo".
#Código Inicial:

#Entrada
numero = float(input('Digite o número: '))

#Processamento
resposta = ""
if numero >= 0:
    resposta = "positivo"
else:
    resposta = "negativo"

#Saída
print("O valor é", resposta)