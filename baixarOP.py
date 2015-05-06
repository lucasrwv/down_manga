import urllib.request
pagina = urllib.request.urlopen(
         #colocar o link do capitulo
         'http://mangareader.xpg.uol.com.br/Online/onepiece-capitulo-351/1414-scansproject'
         )    
texto = pagina.read().decode('utf8')
start_text,end_text = texto.find("pages = [") + 9,texto.find("g\"];") + 2
paginas = texto[start_text:end_text]
a = ["\"",","]
for x in a:
    paginas = paginas.replace(x," ")
paginas = paginas.split()                   
for i in range(0,len(paginas)):
    print (paginas[i])
    urllib.request.urlretrieve(paginas[i],"pagina" + str(i) + ".jpg")
