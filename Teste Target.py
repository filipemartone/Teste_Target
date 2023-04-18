#Questão 1 - resposta: SOMA = 91

#Questão 2

numero = int(input("Digite um número: "))

fibonacci = [0, 1]              #define os casos base da sequência
while fibonacci[-1] < numero:    
    fibonacci.append(fibonacci[-1] + fibonacci[-2]) #adiciona à lista o próximo número da sequência enquanto o último item da lista for menor que o informado

if numero in fibonacci:
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")
    
    
#Questão 3
'''
a) 1, 3, 5, 7, _9_
b) 2, 4, 8, 16, 32, 64, _128_
c) 0, 1, 4, 9, 16, 25, 36, _49_
d) 4, 16, 36, 64, _100_
e) 1, 1, 2, 3, 5, 8, _13_
f) 2, 10, 12, 16, 17, 18, 19, _200_
'''

#Questão 4
'''
Carro: S1 = 0 + 30.t
Caminhão: S2 = 100 - 22.t + 600s
S1 = S2
0 + 30.t = 100 - 22.t + 600s
'''

#Questão 5

s = input("Digite uma string: ")
s_invertida = s[::-1]
print("A string invertida é: ", si)
