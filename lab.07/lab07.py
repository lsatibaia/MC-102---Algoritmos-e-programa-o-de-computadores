q = int(input())
notas = []
pesos = []
laboratorios = []
exames = []
a = 0
x = 0 
y = 0
k = 0
f = 0

for i in range(q):
  n = float(input())
  notas.append(n)

for i in range(q):
  p = int(input())
  pesos.append(p)

while a < q:
  x = x + (notas[a] * pesos[a])
  y = y + pesos[a]
  a = a + 1

media = x / y

if media >= 5:
  print("Media laboratorios:", format(media, ".1f").replace(".", ","))
  print("Situacao: Aprovado por nota")
  print("Nota final:", format(media, ".1f").replace(".", ","))

if media < (5 / 2):
  print("Media laboratorios:", format(media, ".1f").replace(".", ","))
  print("Situacao: Reprovado por nota")
  print("Nota final:", format(media, ".1f").replace(".", ","))

if media >= (5 / 2) and media < 5:
  m = int(input())
  for i in range(m):
    l = int(input())
    laboratorios.append(l)
  
  for i in range(m):
    e = float(input())
    exames.append(e)

  a = 0
  y = 0

  while a < m:
    f = f + (pesos[laboratorios[a]  - 1] * exames[a])
    y = y + pesos[laboratorios[a] - 1]
    a = a + 1
  
  h = f / y
  final = (media + h) / 2

  if final >= 5:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print("Situacao: Aprovado no exame")
    print("Nota final: 5,0")

  if final < 5:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print("Situacao: Reprovado no exame")
    print("Nota final:", format(final, ".1f").replace(".", ","))