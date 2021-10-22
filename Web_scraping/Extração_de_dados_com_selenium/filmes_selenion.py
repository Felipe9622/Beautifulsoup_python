from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from time import sleep

link_site = []

options = Options()

options.add_argument('window-size=1344,659')

navegador = webdriver.Chrome(options=options)

navegador.get('https://torrentool.org/')

sleep(3)

elemento = navegador.find_element_by_tag_name('input')

elemento.send_keys('star wars')
teste = 'star wars'
sleep(3)
elemento.submit()

response = requests.get('https://torrentool.org/index.php?s=' + teste)



content = response.content

site = BeautifulSoup(content, 'html.parser')

programa = site.findAll('div', attrs={'class' : 'capa_lista'})


for frase in programa:
    titulo = frase.find('h3')
    categoria = frase.find('strong')
    idioma = frase.find('span' , attrs={'class' : 'capa_idioma'})
    link = frase.find('a')
    link_site.append([titulo.text, categoria.text, idioma.text, link['href']])


lista = pd.DataFrame(link_site , columns=['titulo' , 'categoria' , 'idioma' , 'link'])

print(lista)
sleep(3)
lista.to_excel('lista_filmes.xlsx' , index = False)