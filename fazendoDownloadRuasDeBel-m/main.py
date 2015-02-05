__author__ = 'andersonmarques'
import urllib.request
import re
response = urllib.request.urlopen("http://kekanto.com.br/ruas/pa/belem")
html = response.read().decode("utf8")

start = 0
while start >= 0:
    start = html.find("<a href=", start)
    start2 = html.find(">", start) + 1
    end = html.find("</a>", start2)
    start = end
    nome_rua = html[start2:end]
    if nome_rua.strip() == "Adicionar um Lugar":
        break

    #existem outros partes do html que batem com o padrão acima e esses casos são tratados aqui.
    if not re.search("est", nome_rua):
        print("Response: %s" % nome_rua)