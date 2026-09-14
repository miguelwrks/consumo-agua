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