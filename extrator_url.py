import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""    

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL esta vazia...")  

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        resultado_match = padrao_url.match(self.url)

        if not resultado_match:
            raise ValueError("A URL não é válida")

        #if self.url.startswith != 'https://':
        #    raise ValueError("A URL nao comeca com https://")    

    def get_url_base(self):
        pos_interrogacao = self.url.find('?')        
        url_base = self.url[:pos_interrogacao] #quando nao é informado a posicao inicial a função adiciona 0
        return url_base

    def get_url_parametros(self):
        pos_interrogacao = self.url.find('?')
        url_parametros = self.url[pos_interrogacao+1:] 
        return url_parametros    

    def get_valor_parametro(self, nome_parametro):       
        indice_parametro = self.get_url_parametros().find(nome_parametro)        

        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)       
        if indice_e_comercial < 0:
            indice_e_comercial = len(self.get_url_parametros())
        valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
                                                  

url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
#parametros = url.get_url_parametros()
#print(parametros)
valor_qtde = url.get_valor_parametro("quantidade")
print(valor_qtde)

moedaOrigem = url.get_valor_parametro("moedaOrigem")
print(moedaOrigem)


import re # Regular Expression - RegEx
endereco = "Rua Serra da Paranapiacaba, nº 189, Adriano Correa, Apucarana - PR, 86813-220"
# 5 digitos + hifen(opcional) + 3 digitos

#O 0-9 significa de zero até 9.: 0 1 2 3 4...
#O simbolo de ? significa que ele pode ser opcional
#O {0,1} é igual ao simbolo ?.. significa que ele pode aparecer de 0 até 1 vez...


padrao_cep = re.compile("[0-9]{5}[-]?[0123456789]{3}")
busca = padrao_cep.search(endereco) # caso a expressão regular possuir valor o retorno é Match

if busca:
    cep = busca.group()
    print(cep)