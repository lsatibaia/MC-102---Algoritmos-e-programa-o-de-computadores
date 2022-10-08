numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
matriz = []

n = ''
while n not in numeros:
  n = input()
  if n not in numeros:
    n = n.split()
    matriz.append(n)
  else: 
    break

n = int(n)
letras = []
palavras = []
for i in range(n):
  b = str(input())
  palavras.append(b)
  b = list(b)
  letras.append(b)

x = 0 
posicao = [[0 for i in range(0)] for j in range(len(palavras))]
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          elif n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          
          elif m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          elif n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          elif n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          elif m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          elif n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          elif n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n] == letras[x][y + 1]:
            m = m - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

x = 0
while x < len(palavras):
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      z = len(palavras[x])
      f = 0
      y = 0
      if matriz[i][j] == letras[x][y]:
        k = i
        l = j
        m = i
        n = j
        f = f + 1
        for h in range(z - 1):
          if n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and y + 2 <= len(palavras[x]) and matriz[m + 1][n] == letras[x][y + 1]:
            m = m + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m + 1][n + 1] == letras[x][y + 1]:
            m = m + 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m - 1][n + 1] == letras[x][y + 1]:
            m = m - 1
            n = n + 1
            y = y + 1
            f = f + 1
          if m + 1 < len(matriz) and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m + 1][n - 1] == letras[x][y + 1]:
            m = m + 1
            n = n - 1
            y = y + 1
            f = f + 1
          elif n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m][n - 1] == letras[x][y + 1]:
            n = n - 1
            y = y + 1
            f = f + 1
          if n + 1 < len(matriz[0]) and y + 2 <= len(palavras[x]) and matriz[m][n + 1] == letras[x][y + 1]:
            n = n + 1
            y = y + 1
            f = f + 1
          if m - 1 >= 0 and n - 1 >= 0 and y + 2 <= len(palavras[x]) and matriz[m - 1][n - 1] == letras[x][y + 1]:
            m = m - 1
            n = n - 1
            y = y + 1
            f = f + 1
          if f == len(palavras[x]):
            if (k + 1 , l + 1) not in posicao[x]:
              posicao[x].append((k + 1 , l + 1))
            f = 0 
            break
      else:
        y = 0
        f = 0
  x = x + 1

for i in range(len(palavras)):
  for j in range(0, len(palavras) - 1):
    if palavras[j] > palavras[j + 1]:
      palavras[j] , palavras[j + 1] = palavras[j + 1] , palavras[j]
      posicao[j] , posicao[j + 1] = posicao[j + 1] , posicao[j]
 
w = 0
u = 0
print(40 * "-")
print("Lista de Palavras")
print(40 * "-")
while u < len(palavras):
  print("Palavra:", palavras[u])
  print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicao[u]])).strip())
  print(40 * "-")
  u = u + 1