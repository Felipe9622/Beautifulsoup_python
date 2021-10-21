import requests
from bs4 import BeautifulSoup
import pandas as pd

link_site = []

response = requests.get('https://torrentool.org/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

programa = site.findAll('div', attrs={'class' : 'capa_lista'})


for frase in programa:
    titulo = frase.find('h3')
    categoria = frase.find('strong')
    idioma = frase.find('span' , attrs={'class' : 'capa_idioma'})
    link = frase.find('a')
    link_site.append([titulo.text, categoria.text, idioma.text, link['href']])

#dataframe cria tabelas que organiza os dados que foram extraidos
#dataframe cria tabelas que organizam a extração de dados
lista = pd.DataFrame(link_site , columns=['titulo' , 'categoria' , 'idioma' , 'link'])

print(lista)#imprime os dados ja acrecentando as tabelas
#prints the data already adding the tables

#converte os dados para excel
#convert data to excel
lista.to_excel('lista_filmes_torrentool.xlsx' , index = False)
