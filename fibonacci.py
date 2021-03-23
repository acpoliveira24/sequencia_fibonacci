"""Sequência de Fibonacci"""


n = int(input('Insira o número de elementos: '))  # Define o número de elementos que a sequência vai ter

elemento = 0  # Definição do elemento da sequência
aux = 0  # Variável auxiliar

for i in range(n):  # Contador dos índices da sequência
    print(elemento)  # Mostra o elemento
    elemento = elemento + aux  # Soma o elemento com a variável auxiliar para gerar o próximo elemento
    aux = elemento - aux  # A variável auxiliar recebe o valor anterior do elemento atual
    if elemento == 0:  # No caso do primeiro elemento, como não há anterior, é somado com 1
        elemento = elemento + 1
