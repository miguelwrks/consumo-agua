#pedir tipo imovel (casa, apartamento ou comerciaal)
#pedir consumo mensal de agua em metros cubicos (1.000 litros) em decimal

#comercial:
#tarifa comercial aplicada

#apartamento:
#ver se o consumo for menor que 10m3 (exibir consumo economico/excelente)

#ap ou casa e consumo de ate 25 (dps de 10 ate 25m3) - consumo moderado dentro do padrao

#qualquer outro caso - cosumo acima do limite residencial - exibir consumo excessivo (e adotar medidas e verificar vazamentos)

#match case pra tipo de imovel, que tem poucas opçoes definidas
#if para consumo, pq varia

print('---> Programa Consumo Agua <---')

imovel = str(input('Digite o tipo do imovel (Casa, Apartamento ou Comercial):'))

consumo_mensal = float(input('Digite o consumo mensal em metros cubicos:'))

match imovel:
    case 'comercial':
        print('Tarifa comercial aplicada, consulte o plano corporativo.')

    case 'apartamento':
        if consumo_mensal<10:
            print('Consum economico - excelente controle de agua')
        elif consumo_mensal >=10 and consumo_mensal<=25:
            print('Consumo moderado - dentro do padrao residencial')
        else:
            print('consumo excessivo - adote medidas de economiaa e verifique vazamentos.')

    case 'casa':
        #nao coloquei ate 10 pq nas instruçoes diziam o consumo ate 10 pro apartamento
        #as outras duas opçoes se repetiram nas duas intrucoes ent coloquei, com a diferença que  no ap eh limitado entre 10 e 25 por causa do consum economico de 10 que ele tem a mais
        if consumo_mensal<=25:
            print('Consumo moderado - dentro do padrao residencial')
        else:
            print('consumo excessivo - adote medidas de economiaa e verifique vazamentos.')

    case _:
        print('opçao de imovel invalida')