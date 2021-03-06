# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série
# de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma
# dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre
# os N primeiros números dessa série.
#
# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).
#
# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco.
# Não deve haver espaço após o último valor.
#
# Exemplo de entrada           Exemplo de saída
#     5                           0 1 1 2 3


n = int(input())

i = 0

t = []

while i < n:

    if i == 0 or i == 1:
        t.append(i)

    if i > 1:
        aux = t[i - 2] + t[i - 1]

        t.append(aux)

    i = i + 1

for j in range(0, n):
    t[j] = str(t[j])

t = ' '.join(t)

print(t)