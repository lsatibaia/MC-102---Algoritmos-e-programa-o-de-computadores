#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
#####################################################
dic = {}
resultados = []

for i in range(16):
  p = str(input())
  dic[p] = [0 , 0 , 0 , 0 , 0 , 0 , 0]

for i in range(16):
  r = input()
  k = r.replace('(', ' ')
  l = k.replace(')', ' ')
  resultados = l.split()
  if len(resultados) == 5:
    int(resultados[1])
    int(resultados[3])
    if resultados[1] > resultados[3]:
      dic[resultados[0]][0] = dic[resultados[0]][0] + 1
      dic[resultados[0]][1] = dic[resultados[0]][1] + 1
      dic[resultados[0]][2] = dic[resultados[0]][2]
      dic[resultados[0]][3] = dic[resultados[0]][3] + 1
      dic[resultados[0]][4] = dic[resultados[0]][4]
      dic[resultados[0]][5] = dic[resultados[0]][5] + int(resultados[1])
      dic[resultados[0]][6] = dic[resultados[0]][6] + int(resultados[3])
      dic[resultados[4]][0] = dic[resultados[4]][0] + 1
      dic[resultados[4]][1] = dic[resultados[4]][1] + 1
      dic[resultados[4]][2] = dic[resultados[4]][2]
      dic[resultados[4]][3] = dic[resultados[4]][3]
      dic[resultados[4]][4] = dic[resultados[4]][4] + 1
      dic[resultados[4]][5] = dic[resultados[4]][5] + int(resultados[3])
      dic[resultados[4]][6] = dic[resultados[4]][6] + int(resultados[1])
    if resultados[1] < resultados[3]:
      dic[resultados[4]][0] = dic[resultados[4]][0] + 1
      dic[resultados[4]][1] = dic[resultados[4]][1] + 1
      dic[resultados[4]][2] = dic[resultados[4]][2]
      dic[resultados[4]][3] = dic[resultados[4]][3] + 1
      dic[resultados[4]][4] = dic[resultados[4]][4]
      dic[resultados[4]][5] = dic[resultados[4]][5] + int(resultados[3])
      dic[resultados[4]][6] = dic[resultados[4]][6] + int(resultados[1])
      dic[resultados[0]][0] = dic[resultados[0]][0] + 1
      dic[resultados[0]][1] = dic[resultados[0]][1] + 1
      dic[resultados[0]][2] = dic[resultados[0]][2]
      dic[resultados[0]][3] = dic[resultados[0]][3]
      dic[resultados[0]][4] = dic[resultados[0]][4] + 1
      dic[resultados[0]][5] = dic[resultados[0]][5] + int(resultados[1])
      dic[resultados[0]][6] = dic[resultados[0]][6] + int(resultados[3])
  if len(resultados) == 8:
    int(resultados[4])
    int(resultados[6])
    if resultados[4] > resultados[6]:
      dic[resultados[0]][0] = dic[resultados[0]][0] + 1
      dic[resultados[0]][1] = dic[resultados[0]][1]
      dic[resultados[0]][2] = dic[resultados[0]][2] + 1
      dic[resultados[0]][3] = dic[resultados[0]][3] + 1
      dic[resultados[0]][4] = dic[resultados[0]][4]
      dic[resultados[0]][5] = dic[resultados[0]][5] + int(resultados[1])
      dic[resultados[0]][6] = dic[resultados[0]][6] + int(resultados[3])
      dic[resultados[7]][0] = dic[resultados[7]][0] + 1
      dic[resultados[7]][1] = dic[resultados[7]][1]
      dic[resultados[7]][2] = dic[resultados[7]][2] + 1
      dic[resultados[7]][3] = dic[resultados[7]][3]
      dic[resultados[7]][4] = dic[resultados[7]][4] + 1
      dic[resultados[7]][5] = dic[resultados[7]][5] + int(resultados[3])
      dic[resultados[7]][6] = dic[resultados[7]][6] + int(resultados[1])
    if resultados[4] < resultados[6]:
      dic[resultados[7]][0] = dic[resultados[7]][0] + 1
      dic[resultados[7]][1] = dic[resultados[7]][1]
      dic[resultados[7]][2] = dic[resultados[7]][2] + 1
      dic[resultados[7]][3] = dic[resultados[7]][3] + 1
      dic[resultados[7]][4] = dic[resultados[7]][4]
      dic[resultados[7]][5] = dic[resultados[7]][5] + int(resultados[3])
      dic[resultados[7]][6] = dic[resultados[7]][6] + int(resultados[1])
      dic[resultados[0]][0] = dic[resultados[0]][0] + 1
      dic[resultados[0]][1] = dic[resultados[0]][1]
      dic[resultados[0]][2] = dic[resultados[0]][2] + 1
      dic[resultados[0]][3] = dic[resultados[0]][3]
      dic[resultados[0]][4] = dic[resultados[0]][4] + 1
      dic[resultados[0]][5] = dic[resultados[0]][5] + int(resultados[1])
      dic[resultados[0]][6] = dic[resultados[0]][6] + int(resultados[3])

f = list(dic.keys())
for i in range(0, 16):
  print("-" * 50)
  print("Pais:", f[i])
  print("Partidas:", dic[f[i]][0])
  print("Partidas decididas em tempo normal de jogo:", dic[f[i]][1])
  print("Partidas decicidas nos penaltis:", dic[f[i]][2])
  print("Vitorias:", dic[f[i]][3])
  print("Derrotas:", dic[f[i]][4])
  print("Gols marcados:", dic[f[i]][5])
  print("Gols sofridos:", dic[f[i]][6])

for i in range(0, 16):
  if dic[f[i]][0] == 4 and dic[f[i]][4] == 0:
    print("-" * 50)
    print("Pais campeao:", f[i])
    print("-" * 50)