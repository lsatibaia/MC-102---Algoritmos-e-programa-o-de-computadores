n = int(input())
acoes = []
valores = []
a = 0
b = 1
ma = -1
valor = 0

for i in range(n):
  ac = float(input())
  acoes.append(ac)

k = int(input())
q = float(input())

for i in acoes:
  while a < n - 1:
    if b < n and b <= k + a:
      while b <= k + a and b < n:
        x = acoes[a] - acoes[b]
        l = (-1) * x * (q // acoes[a])
        if l > ma:
          ma = l
          dc = a + 1
          vc = acoes[a]
          dv = b + 1
          vv = acoes[b]
          valor = x * (-1)
          b = b + 1
        else:
          b = b + 1        
        if b > n:
          a = a + 1
          b = a + 1
    else: 
      a = a + 1
      b = a + 1

if valor <= 0:
  dc = 1
  dv = 1
  vc = acoes[0]
  vv = acoes[0]
  quantidade = q // vc
  lucro = 0.00
if valor > 0:
  quantidade = q // vc
  lucro = valor * quantidade


print('Dia da compra:', dc)
print('Valor de compra: R$', format(vc, '.2f').replace('.', ','))
print('Dia da venda:', dv)
print('Valor de venda: R$', format(vv, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', format(quantidade, '.0f'))
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))