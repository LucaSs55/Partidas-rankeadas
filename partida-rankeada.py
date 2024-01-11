while True:
    v = int(input('Quantidade de vitórias:'))
    d = int(input('Quantidade de derrotas:'))
    saldo = v - d
    nivel = ' '
    if v <= 10:
        nivel = 'Ferro'
    elif v >= 11 and v <= 20:
        nivel = 'bronze'
    elif v >= 21 and v <= 50:
        nivel = 'prata'
    elif v >= 51 and v <= 80:
        nivel = 'Ouro'
    elif v >= 81 and v <= 90:
        nivel = 'diamante'
    elif v >= 91 and v <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'imortal'
    opção = str(input('Deseja tentar novamente?[S/N]:')).strip().upper()
    if opção in 'N':
        break
print(f'O herói tem saldo de vitórias {saldo} e está no nível {nivel}')