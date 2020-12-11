from urllib.request import urlopen

def instrucciones():
  url = "https://es.wikipedia.org/wiki/Buscaminas#Reglas"
  page = urlopen(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  title_index = html.find('<h2><span class="mw-headline" id="Reglas">Reglas</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Buscaminas&amp;action=edit&amp;section=2" title="Editar sección: Reglas">editar</a><span class="mw-editsection-bracket">]</span></span></h2>')
  start_index = title_index + len('<h2><span class="mw-headline" id="Reglas">Reglas</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Buscaminas&amp;action=edit&amp;section=2" title="Editar sección: Reglas">editar</a><span class="mw-editsection-bracket">]</span></span></h2>')
  end_index = html.find('<h3><span class="mw-headline" id="Niveles_de_Juego"')
  reglas = html[start_index:end_index]
  texto = ''
  x = 0
  indice = 0
  for i in reglas:
    if i == '>':
      x = indice + 1
    if i == '<':
      texto = texto + reglas[x:indice]
    indice += 1
  
  return texto

print('Reglas del juego:')
print(instrucciones())
