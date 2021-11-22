import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

#pesquisa o produto como se fosse na aba de pesquisa do proprio site ex: moto g5
#write the product as if you were searching on the site itself, exemple : moto g5
escolha = input('qual produto que deseja pesquisar ? :')

response = requests.get(url_base + escolha)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class' : 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class' : 'ui-search-item__title'})
    real = produto.find('span', attrs={'class' : 'price-tag-fraction'})
    link = produto.find('a' , attrs={'ui-search-item__group__element ui-search-link'})
    lista_produtos.append([titulo.text, real.text, link['href']])


lista = pd.DataFrame(lista_produtos , columns=['titulo' , 'valor R$' , 'link'])

print(lista)#imprime os dados ja acrecentando as tabelas
#prints the data already adding the tables

lista.to_excel('lista_de_produtos.xlsx' , index = False)



