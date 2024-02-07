def conversao_binario(n):
    if n > 1:
        binarios = str('')
        while n >= 2:
            if n // 2 > 1:
                binarios += str(n % 2)
            else:
                binarios += str(n % 2) + str(n//2)
            n = n // 2
        return binarios[::-1]
    elif n == 1:
        return 1
    else:
        return 0


while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        if numero < 0:
            raise ValueError
        break
    except ValueError:
        print('Digite apenas números positivos.')

binario = conversao_binario(numero)
print(f'''-------------------------------------------
Número na base decimal: {numero}
-------------------------------------------''')
print(f'Conversão para base binária: {binario}')
