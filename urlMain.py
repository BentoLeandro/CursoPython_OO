#"https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

url = '      '

#Sanitização da URL
url = url.strip() #neste caso o strip é melhor que o url.replace(" ", "") 
                  #pq ele retira tb a tabulacao como exem.: \t

#Validação da URL
if url == "":
    raise ValueError("A URL esta vazia...")

#Separa base e os parametros
pos_interrogacao = url.find('?')
qtde_caracteres = len(url)
url_base = url[:pos_interrogacao] #quando nao é informado a posicao inicial a função adiciona 0
print(url_base)

url_parametros = url[pos_interrogacao+1:] #quando nao é informado a posicao final 
                                          #a funcao entende que será até o ultimo caracteres
print(url_parametros)

#Busca o valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
print(indice_e_comercial)
if indice_e_comercial < 0:
    indice_e_comercial = len(url_parametros)
valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
