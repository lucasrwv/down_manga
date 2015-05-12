import urllib.request
print("baixe qualquer capitulo de one piece")
nucap = input("digite o numero do capitulo: ")
#procura o link do capitulo
pag1 = urllib.request.urlopen(
    'http://mangareader.xpg.uol.com.br/Online/onepiece-capitulo-0/36742-strawhatscans#/!page0')
text1 = pag1.read().decode('utf-8')
inicio = text1.find("<!--<center><img src=\"/assets/images/loading.gif\"></center>-->")
text1 = text1[inicio:]
end_url = text1.find("Cap. " + nucap + "<") - 62
start_url = text1.find("capitulo-" + nucap + "/") - 50
url1 = text1[start_url:end_url]
#baixa as paginas
pagina = urllib.request.urlopen(url1)    
texto = pagina.read().decode("utf-8")
start_text,end_text = texto.find("pages = [") + 9,texto.find("\"];") + 1
paginas = texto[start_text:end_text]
a = ["\"",","]
for x in a:
    paginas = paginas.replace(x," ")
paginas = paginas.split()
for i in range(0,len(paginas)):
    print("baixando %d/%d" %(i+1,len(paginas)))
    urllib.request.urlretrieve(paginas[i],"pagina" + str(i) + ".jpg")


    
