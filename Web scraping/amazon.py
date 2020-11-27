import scrapy


# scrapy runspider amazon.py roda script do programa no terminal 
# scrapy crawl amazon -o extrção_arquivos_amazon4.csv para extrair os aquivos do script para excell no termial 


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2']

    def parse(self, response):
        all_div = response.css('.sg-col-inner')
        modelo = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[0].extract()
        valor = all_div.xpath("//span[@class='a-price-whole']/text()")[0].extract()
        modelo1 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[2].extract()
        valor1 = all_div.xpath("//span[@class='a-price-whole']/text()")[2].extract()
        modelo2 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[3].extract()
        valor2 = all_div.xpath("//span[@class='a-price-whole']/text()")[3].extract()
        modelo3 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[4].extract()
        valor3 = all_div.xpath("//span[@class='a-price-whole']/text()")[4].extract()
        modelo4 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[5].extract()
        valor4 = all_div.xpath("//span[@class='a-price-whole']/text()")[5].extract()
        modelo5 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[6].extract()
        valor5 = all_div.xpath("//span[@class='a-price-whole']/text()")[6].extract()
        modelo6 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[7].extract()
        valor6= all_div.xpath("//span[@class='a-price-whole']/text()")[7].extract()
        modelo7 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[9].extract()
        valor7 = all_div.xpath("//span[@class='a-price-whole']/text()")[9].extract()
        modelo8 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[10].extract()
        valor8 = all_div.xpath("//span[@class='a-price-whole']/text()")[10].extract()
        modelo9 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[11].extract()
        valor9= all_div.xpath("//span[@class='a-price-whole']/text()")[11].extract()
        modelo10 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[13].extract()
        valor10= all_div.xpath("//span[@class='a-price-whole']/text()")[13].extract()
        modelo11 = all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[14].extract()
        valor11= all_div.xpath("//span[@class='a-price-whole']/text()")[14].extract()
        modelo12= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[16].extract()
        valor12= all_div.xpath("//span[@class='a-price-whole']/text()")[16].extract()
        modelo13= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[17].extract()
        valor13= all_div.xpath("//span[@class='a-price-whole']/text()")[17].extract()
        modelo14= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[19].extract()
        valor14= all_div.xpath("//span[@class='a-price-whole']/text()")[19].extract()
        modelo15= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[21].extract()
        valor15= all_div.xpath("//span[@class='a-price-whole']/text()")[21].extract()
        modelo16= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[23].extract()
        valor16= all_div.xpath("//span[@class='a-price-whole']/text()")[23].extract()
        modelo17= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[24].extract()
        valor17= all_div.xpath("//span[@class='a-price-whole']/text()")[24].extract()
        modelo18= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[25].extract()
        valor18= all_div.xpath("//span[@class='a-price-whole']/text()")[25].extract()
        modelo19= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[27].extract()
        valor19= all_div.xpath("//span[@class='a-price-whole']/text()")[27].extract()
        modelo20= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[28].extract()
        valor20= all_div.xpath("//span[@class='a-price-whole']/text()")[28].extract()
        modelo21= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[29].extract()
        valor21= all_div.xpath("//span[@class='a-price-whole']/text()")[29].extract()
        modelo22= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[30].extract()
        valor22= all_div.xpath("//span[@class='a-price-whole']/text()")[30].extract()
        modelo23= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[34].extract()
        valor23= all_div.xpath("//span[@class='a-price-whole']/text()")[34].extract()
        modelo24= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[35].extract()
        valor24= all_div.xpath("//span[@class='a-price-whole']/text()")[35].extract()
        modelo25= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[36].extract()
        valor25= all_div.xpath("//span[@class='a-price-whole']/text()")[36].extract()
        modelo26= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[37].extract()
        valor26= all_div.xpath("//span[@class='a-price-whole']/text()")[37].extract()
        modelo27= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[38].extract()
        valor27= all_div.xpath("//span[@class='a-price-whole']/text()")[38].extract()
        modelo28= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[39].extract()
        valor28= all_div.xpath("//span[@class='a-price-whole']/text()")[39].extract()
        modelo29= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[39].extract()
        valor29= all_div.xpath("//span[@class='a-price-whole']/text()")[39].extract()
        modelo30= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[40].extract()
        valor30= all_div.xpath("//span[@class='a-price-whole']/text()")[40].extract()
        modelo31= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[41].extract()
        valor31= all_div.xpath("//span[@class='a-price-whole']/text()")[41].extract()
        modelo32= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[42].extract()
        valor32= all_div.xpath("//span[@class='a-price-whole']/text()")[42].extract()
        modelo33= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[43].extract()
        valor33= all_div.xpath("//span[@class='a-price-whole']/text()")[43].extract()
        modelo34= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[44].extract()
        valor34= all_div.xpath("//span[@class='a-price-whole']/text()")[44].extract()
        modelo35= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[45].extract()
        valor35= all_div.xpath("//span[@class='a-price-whole']/text()")[45].extract()
        modelo36= all_div.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[47].extract()
        valor36= all_div.xpath("//span[@class='a-price-whole']/text()")[47].extract()

        yield {
            'modelo': modelo,
            'valor' : valor,
            'modelo1': modelo1,
            'valor1': valor1,
            'modelo2': modelo2,
            'valor2': valor2,
            'modelo3': modelo3,
            'valor3': valor3,
            'modelo4': modelo4,
            'valor4': valor4,
            'modelo5': modelo5,
            'valor5': valor5,
            'modelo6': modelo6,
            'valor6': valor6,
            'modelo7': modelo7,
            'valor7': valor7,
            'modelo8': modelo8,
            'valor8': valor8,
            'modelo9': modelo9,
            'valor9': valor9,
            'modelo10': modelo10,
            'valor10': valor10,
            'modelo11': modelo11,
            'valor11': valor11,
            'modelo12': modelo12,
            'valor12': valor12,
            'modelo13': modelo13,
            'valor13': valor13,
            'modelo14': modelo14,
            'valor14': valor14,
            'modelo15': modelo15,
            'valor15' : valor15,
            'modelo16': modelo16,
            'valor16' : valor16,
            'modelo17': modelo17,
            'valor17' : valor17,
            'modelo18': modelo18,
            'valor18' : valor18,
            'modelo19': modelo19,
            'valor19' : valor19,
            'modelo20': modelo20,
            'valor20' : valor20,
            'modelo21': modelo21,
            'valor21' : valor21,
            'modelo22': modelo22,
            'valor22' : valor22,
            'modelo23': modelo23,
            'valor23' : valor23,
            'modelo24': modelo24,
            'valor24' : valor24,
            'modelo25': modelo25,
            'valor25' : valor25,
            'modelo26': modelo26,
            'valor26' : valor26,
            'modelo27': modelo27,
            'valor27' : valor27,
            'modelo28': modelo28,
            'valor28' : valor28,
            'modelo29': modelo29,
            'valor29' : valor29,
            'modelo30': modelo30,
            'valor30' : valor30,
            'modelo31': modelo31,
            'valor31' : valor31,
            'modelo32': modelo32,
            'valor32' : valor32,
            'modelo33': modelo33,
            'valor33' : valor33,
            'modelo34': modelo34,
            'valor34' : valor34,
            'modelo35': modelo35,
            'valor35' : valor35,
            'modelo36': modelo36,
            'valor36' : valor36,
        }