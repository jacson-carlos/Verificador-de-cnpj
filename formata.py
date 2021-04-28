from itertools import count


def limpa(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def primeiro_digito(cnpj):
    cnpja = limpa(cnpj)
    contador = count(5, -1)
    cinco_primeiros = [int(x) for x in cnpja[0:4]]
    zip_cinco = zip(contador, cinco_primeiros)

    contador = count(9, -1)
    nove_proximos = [int(x) for x in cnpja[4:12]]
    zip_nove = zip(contador, nove_proximos)

    soma_cinco = [x * y for x, y in zip_cinco]
    sum_cinco = 0
    for x in soma_cinco:
        sum_cinco += x
    soma_nove = [x * y for x, y in zip_nove]
    sum_nove = 0
    for y in soma_nove:
        sum_nove += y

    return sum_cinco + sum_nove


def gera_digito(primeiro_dig):
    valida = 11 - (primeiro_dig % 11)

    if valida > 9:
        valida = 0

    return valida


def segundo_digito(cnpj):
    cnpja = limpa(cnpj)
    contador = count(6, -1)
    seis_primeiros = [int(x) for x in cnpja[0:5]]
    zip_seis = zip(contador, seis_primeiros)

    contador = count(9, -1)
    nove_proximos = [int(x) for x in cnpja[5:13]]
    zip_nove = zip(contador, nove_proximos)

    soma_seis = [x * y for x, y in zip_seis]
    sum_seis = 0
    for x in soma_seis:
        sum_seis += x
    soma_nove = [x * y for x, y in zip_nove]
    sum_nove = 0
    for y in soma_nove:
        sum_nove += y

    return sum_seis + sum_nove


def adiciona_dig(lista, x, y):
    lista.append(x)
    lista.append(y)
    return lista


def validacao(cnpj, cnpj_gerado):
    if cnpj == cnpj_gerado:
        return 'O CNPJ é válido'
    else:
        return 'o CNPJ não é válido'

