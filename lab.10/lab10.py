numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
matriz = []
#ler o caça palavras
n = ''
while n not in numeros:
  n = input()
  if n not in numeros:
    n = n.split()
    matriz.append(n)
  else: 
    break

#ler o numero de palavras e as palavras buscadas 
n = int(n)
busca = []
a = 0
palavras = []
while a < n:
  b = str(input())
  palavras.append(b)
  b = list(b)
  busca.append(b)
  a = a + 1 

#achar as palavras buscadas
l = len(matriz)
c = len(matriz[0])
p = len(busca)
iguais = [0 for i in range(p)]
a = 0
pa = 0
t = 0
posicao = {'horizontal': [], 'vertical': [], 'diagonal para baixo': [], 'diagonal para cima': []}

#horizontal
m = 0
n = 0
pa = 0
a = 0
t = 0
while a < p:
  h = len(busca[a])
  while m < l:
    while n <= c - h:
      if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
        t = t + 1 
        pa = pa + 1
        x = m
        y = n
        m = m
        n = n + 1
        while t < h:
          if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
            t = t + 1
            m = m
            n = n + 1
            pa = pa + 1
            if pa == h:
              iguais[a] = iguais[a] + 1
              posicao['horizontal'] = posicao['horizontal'] + [x, y, h]
              n = y + 1
              m = x 
              pa = 0
              t = 0
          if busca[a][t] != matriz[m][n] and matriz[m][n] != '*':
            t = 0
            pa = 0
            m = x 
            n = y + 1
            break
      n = n + 1
    n = 0
    m = m + 1
  a = a + 1
  m = 0
  n = 0

    
#vertical
m = 0
n = 0
pa = 0
a = 0
t = 0
while a < p:
  h = len(busca[a])
  while n < c:
    while m <= l - h:
      if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
        t = t + 1 
        pa = pa + 1
        x = m
        y = n
        m = m + 1
        n = n
        while t < h:
          if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
            t = t + 1
            m = m + 1
            n = n
            pa = pa + 1
            if pa == h:
              iguais[a] = iguais[a] + 1
              posicao['vertical'] = posicao['vertical'] + [x, y, h]
              n = y 
              m = x + 1
              pa = 0
              t = 0
          if busca[a][t] != matriz[m][n] and matriz[m][n] != '*':
            t = 0
            pa = 0
            m = x + 1
            n = y
            break
      m = m + 1
    m = 0
    n = n + 1
  a = a + 1
  m = 0
  n = 0

#diagonal para baixo 
m = 0
a = 0
n = 0
pa = 0
t = 0
while a < p:
  h = len(busca[a])
  while m <= l - h:
    while n <= c -h:
      if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
        t = t + 1 
        pa = pa + 1
        x = m
        y = n
        m = m + 1
        n = n + 1
        while t < h:
          if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
            t = t + 1
            m = m + 1
            n = n + 1
            pa = pa + 1
            if pa == h:
              iguais[a] = iguais[a] + 1
              posicao['diagonal para baixo'] = posicao['diagonal para baixo'] + [x, y, h]
              n = y + 1
              m = x 
              pa = 0
              t = 0
          if busca[a][t] != matriz[m][n] and matriz[m][n] != '*':
            t = 0
            pa = 0
            m = x 
            n = y
            break
      n = n + 1
    n = 0
    m = m + 1
  a = a + 1
  m = 0
  n = 0

#diagonal para cima
m = l - 1
n = 0
a = 0
pa = 0
t = 0
while a < p:
  h = len(busca[a])
  while m >= l - h:
    while n <= c -h:
      if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
        t = t + 1 
        pa = pa + 1
        x = m
        y = n
        m = m - 1
        n = n + 1
        while t < h:
          if busca[a][t] == matriz[m][n] or matriz[m][n] == '*':
            t = t + 1
            m = m - 1
            n = n + 1
            pa = pa + 1
            if pa == h:
              iguais[a] = iguais[a] + 1
              posicao['diagonal para cima'] = posicao['diagonal para cima'] + [x, y, h]
              n = y + 1
              m = x 
              pa = 0
              t = 0
          if busca[a][t] != matriz[m][n] and matriz[m][n] != '*':
            t = 0
            pa = 0
            m = x 
            n = y
            break
      n = n + 1
    n = 0
    m = m - 1
  a = a + 1
  m = l - 1
  n = 0



# colocas as palavras achadas em maiusculo
#horizontal
e = 0
m = len(posicao['horizontal'])
while e < m:
  if e < m:
    y = posicao['horizontal'][e]
    x = posicao['horizontal'][e + 1]
    f = posicao['horizontal'][e + 2]
    n = 0
    while n < f:
      matriz[y][x + n] = matriz[y][x + n].upper()
      n = n + 1
  e = e + 3

#vertical
e = 0
m = len(posicao['vertical'])
while e < m:
  if e < m:
    y = posicao['vertical'][e]
    x = posicao['vertical'][e + 1] 
    f = posicao['vertical'][e + 2]
    n = 0
    while n < f:
      matriz[y + n][x] = matriz[y + n][x].upper()
      n = n + 1
  e = e + 3

#diagonal para baixo 
e = 0
m = len(posicao['diagonal para baixo'])
while e < m:
  if e < m:
    y = posicao['diagonal para baixo'][e] 
    x = posicao['diagonal para baixo'][e + 1]
    f = posicao['diagonal para baixo'][e + 2]
    n = 0
    while n < f:
      matriz[y + n][x + n] = matriz[y + n][x + n].upper()
      n = n + 1
  e = e + 3

#diagonal para cima
e = 0
m = len(posicao['diagonal para cima'])
while e < m:
  if e < m:
    y = posicao['diagonal para cima'][e]
    x = posicao['diagonal para cima'][e + 1]
    f = posicao['diagonal para cima'][e + 2]
    n = 0
    while n < f:
      matriz[y - n][x + n] = matriz[y - n][x + n].upper()
      n = n + 1
  e = e + 3


#imprimir a quandidade de palavras encontradas
print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
a = 0
while a < p:
  print('Palavra:', palavras[a])
  print('Ocorrencias:', iguais[a])
  print("-" * 40)
  a = a + 1

#imprimir o novo caça 
for i in range(l):
  print(" ".join(matriz[i]))