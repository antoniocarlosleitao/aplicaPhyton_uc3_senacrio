#2. Questão 2: Par ou Ímpar
#   Enunciado: Solicite um número do usuário e use `if-else` para determinar se o número é par ou ímpar.
#   Imprima o resultado apropriado.

#Entrada
numero = int(input("Digite um número: "))

#Processamento
resposta = ""
if numero % 2 == 0:
    resposta = "par"
else:
    resposta = "impar"

#Saída
print("O número é", resposta)

