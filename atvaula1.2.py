#2. Questão 2: Checagem de Divisibilidade
#   - Enunciado: Peça ao usuário para inserir um número e verifique se ele é divisível por 5. Se o número for divisível por 5, imprima "Divisível por 5".
#Código Inicial:

#Entrada
numero = int(input("Digite um número: "))

#Processamento
if(numero % 5 == 0):
    print('Divisível por 5')
else:
    print('Não divisível por 5')


