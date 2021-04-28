while True:
    from formata import limpa, primeiro_digito, gera_digito, \
    segundo_digito, adiciona_dig, validacao



    cnpj = input('Digite o CNPJ para validação: ')

    cnpj_sem_carac= limpa(cnpj)
    cnpj_lista = []
    for x in cnpj_sem_carac:
        cnpj_lista.append(int(x))

    primeiro_digito = primeiro_digito(cnpj)
    digito1 = int(gera_digito(primeiro_digito))

    seg_digito = segundo_digito(cnpj)
    digito2 = gera_digito(seg_digito)

    cnpj_limpo = cnpj_sem_carac[0:12]
    novo_cnpj=[]

    for i in cnpj_limpo:
        novo_cnpj.append(int(i))


    cnpj_gerado = novo_cnpj.copy()

    adiciona_dig(cnpj_gerado, digito1, digito2)

    resultado = validacao(cnpj_lista, cnpj_gerado)
    print(resultado)