dados = []
a = input()
a = a.split()
dados.append(a)

tab = []
b = int(dados[0][0])
c = int(dados[0][1])
for i in range(b):
  d = input()
  d = d.split()
  tab.append(d)

pontos = []
e = input()
e = e.split()
pontos.append(e)
f = input()
f = f.split()
pontos.append(f)

for i in range(b):
  for j in range(c):
    tab[i][j] = int(tab[i][j])

xi = int(pontos[0][0])
yi = int(pontos[0][1])
xf = int(pontos[1][0])
yf = int(pontos[1][1])

cam = [0 , 0]
if c > 25:
  cam = [0 , 1]
   
if tab[xi][yi] != 0:
  n = []
  s = []
  x = xi
  y = yi
  g = tab[x][y]
  s.append((x , y , g))
  for k in range(b * c):
    n = s
    s = []
    for l in range(0, len(n)):
      if len(n) == 0:
        break
      o = n[l][0]
      p = n[l][1]
      q = n[l][2]
      if o + q < b and tab[o + q][p] != 0:
        s.append((o + q , p , tab[o + q][p]))
      if o - q < b and 0 <= o - q and tab[o - q][p] !=  0:
        s.append((o - q , p , tab[o - q][p]))           
      if p + q < c and tab[o][p + q] != 0:
        s.append((o , p + q , tab[o][p + q]))
      if p - q < c and 0 <= p - q and tab[o][p - q] != 0:
        s.append((o , p - q , tab[o][p - q]))
      if o + q == xf and p == yf:
        cam[0] = 1
        break
      if o - q == xf and p == yf:
        cam[0] = 1
        break
      if o == xf and p + q == yf:
        cam[0] = 1
        break
      if o == xf and p - q == yf:
        cam[0] = 1
        break
      if len(s) > 1000 and cam[0] != 0:
        break
      if len(s) > 1000 and cam[1] != 0:
        break
      if len(s) > 100000:
        break
          
cam[1] = 0          
if tab[xf][yf] != 0:
  n = []
  s = []
  x = xf
  y = yf
  g = tab[x][y]
  s.append((x , y , g))
  for k in range(b * c):
    n = s
    s = []
    for l in range(0, len(n)):
      if len(n) == 0:
        break
      o = n[l][0]
      p = n[l][1]
      q = n[l][2]
      if o + q < b and tab[o + q][p] != 0:
        s.append((o + q , p , tab[o + q][p]))
      if o - q < b and 0 <= o - q and tab[o - q][p] !=  0:
        s.append((o - q , p , tab[o - q][p]))           
      if p + q < c and tab[o][p + q] != 0:
        s.append((o , p + q , tab[o][p + q]))
      if p - q < c and 0 <= p - q and tab[o][p - q] != 0:
        s.append((o , p - q , tab[o][p - q]))
      if o + q == xi and p == yi:
        cam[1] = 1
        break
      if o - q == xi and p == yi:
        cam[1] = 1
        break
      if o == xi and p + q == yi:
        cam[1] = 1
        break
      if o == xi and p - q == yi:
        cam[1] = 1
        break
      if len(s) > 1000 and cam[1] != 0:
        break
      if len(s) > 1000 and cam[0] != 0:
        break      
      if len(s) > 100000:
        break
      
if cam[0] == 0:
  print("({},{}) -> ({},{}): nao existe caminho".format(xi, yi, xf,yf))
if cam[0] == 1:
  print("({},{}) -> ({},{}): existe caminho".format(xi, yi, xf,yf))
if cam[1] == 0:
  print("({},{}) -> ({},{}): nao existe caminho".format(xf, yf, xi,yi))
if cam[1] == 1:
  print("({},{}) -> ({},{}): existe caminho".format(xf, yf, xi, yi))
