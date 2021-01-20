import requests
from bs4 import BeautifulSoup
import csv

# Vamos mudar a URL
url = 'https://www.amazon.com.br/s?k=aplle+wach&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3IMJ859FBOT7H&sprefix=aplle%2Caps%2C265&ref=nb_sb_ss_ts-a-p_3_5'

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

# lendo a URL com a urllopenr
html = requests.get(url=url, headers=headers)

# Enfim mostrando o poder da bs4
bs = BeautifulSoup(html.text, 'html.parser')

produto = bs.find('div' , {'class' : 'sg-col-inner'})
#imprime titulo da pagina 
teste = bs.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
# a [] funciona como uma bussola para qual dado do relogio especifico deseja, caso retire ele vai pegar o nome de todos os relogerios na pagina 

lista_relogios = []

for item in teste:
	lista_relogios.append(item)
	print(item.text)



with open('relogio2.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter = ',')
	for item in lista_relogios:
		spamwriter.writerow([item.text])



