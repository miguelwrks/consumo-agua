import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print('---> Programa Consumo Agua <---')

imovel = str(input('Digite o tipo do imovel (Casa, Apartamento ou Comercial):'))

consumo_mensal = float(input('Digite o consumo mensal em metros cubicos:'))

match imovel:
    case 'comercial':
        clear()
        print('Tarifa comercial aplicada, consulte o plano corporativo.')

    case 'apartamento':
        clear()
        if consumo_mensal<10:
            print('Consum economico - excelente controle de agua')
        elif consumo_mensal >=10 and consumo_mensal<=25:
            print('Consumo moderado - dentro do padrao residencial')
        else:
            print('consumo excessivo - adote medidas de economiaa e verifique vazamentos.')

    case 'casa':
        #nao coloquei ate 10 pq nas instruçoes diziam o consumo ate 10 pro apartamento
        #as outras duas opçoes se repetiram nas duas intrucoes ent coloquei, com a diferença que  no ap eh limitado entre 10 e 25 por causa do consum economico de 10 que ele tem a mais
        clear()
        if consumo_mensal<=25:
            print('Consumo moderado - dentro do padrao residencial')
        else:
            print('consumo excessivo - adote medidas de economiaa e verifique vazamentos.')

    case _:
        print('opçao de imovel invalida')

