print(f'\033[40;33;1m{"Desafio 53":=^20}\033[m\n\033[40;31;1m{"PALINDROMOR":^20}\033[m')
frase = input('Dígite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase não é um palindromo')