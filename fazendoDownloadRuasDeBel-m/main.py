__author__ = 'andersonmarques'
import urllib.request

response = urllib.request.urlopen("http://kekanto.com.br/ruas/pa/belem")
html = response.read().decode("utf8")

start = 0
while start < 0:
    start = html.find("<a href=", start)
    start2 = html.find(">", start) + 1
    end = html.find("</a>", start2)

    nome_rua = html[start2:end]
    if nome_rua.strip() == "Adicionar um Lugar":
        break
    start = end
    print("Response: %s" % nome_rua)