import requests
from bs4 import BeautifulSoup
import pandas as pd
listanomes = []
listaprecos = []
listadesc = []

r = requests.get("http://10.109.69.5/ProjetoIntegrador%20LIMA%20-%20Gabriel%20Pimentel/index.html")
soup = BeautifulSoup(r.content, "html.parser")
s = soup.find('div', class_="produtos")

tituloproduto = s.find_all('h1')
for c in tituloproduto:
    listanomes.append(c.text)

precoprodutos = s.find_all('h2')
for c in precoprodutos:
    listaprecos.append(c.text)

descricaoprodutos = s.find_all('h3')
for c in descricaoprodutos:
    listadesc.append(c.text)

lista = {"Nomes": listanomes, "Preços": listaprecos, "Descrição": listadesc}
print(lista)
listateste = pd.DataFrame(lista)
listateste.to_excel("projetointegrador-Gabriel.xlsx")
print(listateste)
