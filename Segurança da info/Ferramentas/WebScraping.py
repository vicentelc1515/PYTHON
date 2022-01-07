#pega os códigos html dos sites!!
# quais quiser!!!

from bs4 import BeautfulSoup
import request

site = request.get("https://www.climatempo.com.br/").content

soup = BeautfulSoup(site, 'html.parser')
#baixando do site o html
print(soup.prettify())
# transforma o html em string e o print exibe isso
temperatura = soup.find("span", class = "_block _margin-b-5 - grav")