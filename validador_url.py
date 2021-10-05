import re

"""
Expressoes Regulares
[] indica que o texto ou numero pode ser 1 ou mais caracteres, exemplo,
   caso seja informado [0123456789], se o valor informado for 3 ja vai ser encontrado.
() indica que o texto deve ser exatamente igual, exemplo, (012345),
   se for informado somente o 3 o padrao não vai encontrar, é obrigatorio ser o mesmo valor
?  o simbolo de interrogação indica que o parametro pode ser opcional

-  quando o texto ou numero estiver sendo separado por hifen(-) indica que vai ser um
   intervalor de valores, exemplo, 0-5 é igual 012345.

texto solto - quando o texto for obrigatorio e exatamente igual ao informado, nao pe necessario
              informar as chaves () pode informar o texto direto  

um parametro pode ter outro parametro dentro dele, como opcional, exemplo, 
a url pode ser http ou https, (http(s)?)                   

search = metodo utilizado para pesquisar um padrão dentro de um texto. 
         pesquisar um cep dentro de um endereço completo..

match = metodo utilizado para pesquisar o texto inteiro como padrão, caso o texto 
        não estiver dentro do padrao nao vai ser localizado         

"""

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
resultado_match = padrao_url.match(url)

if not resultado_match:
    raise ValueError("A URL não é válida")

print("URL é válida...")    