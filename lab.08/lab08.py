###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
###################################################
x = int(input())
a = 0
b = ''
c = ' '
pontuacao = (".", ",", ":", ";", "!", "?")

while a < x:
  y = str(input())
  y = y.upper()
  b = b + c + y
  a = a + 1

for p in pontuacao:
  b = b.replace(p , ' ')

texto = b.split()
textos = texto.copy()
texto = " ".join(texto)

z = int(input())
a = 0
b = ''
letras = []
d = []

while a < z:
  p = str(input())
  d.append(p)
  p = p.upper()
  l = len(p)
  letras.append(l)
  b = b + c + p
  a = a + 1

palavras = b.split()
q = len(palavras)
l = len(textos)

a = 0 
iguais = 0
semelhantes = 0

while a < q:
  s = texto.count(palavras[a])
  t = texto.count(c + palavras[a] + c)
  u = texto.count(c + palavras[a] + c + palavras[a] + c)
  if textos[0] == palavras[a] or textos[l - 1] == palavras[a]:
    print("Palavra buscada:", d[a])
    print("Ocorrencia:", t + u + 1)
    print("Palavras similares:", s - t - u - 1)
  elif textos[0] == palavras[a] and textos[l - 1] == palavras[a]:
    print("Palavra buscada:", d[a])
    print("Ocorrencia:", t + u + 2)
    print("Palavras similares:", s - t - u - 2)
  else:
    print("Palavra buscada:", d[a])
    print("Ocorrencia:", t + u)
    print("Palavras similares:", s - t - u)
  a = a + 1