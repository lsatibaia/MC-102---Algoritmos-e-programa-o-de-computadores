###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
###################################################

x = float(input())
print("Bruto: R$", format(x, ".2f").replace(".", ","))

if x <= 1045.00 :
 y = x - (0.925 * x)
if 1045.01 <= x <= 2089.60 :
 y = x - (0.91 * x)
if 2089.61 <= x <= 3134.40 :
 y = x - (0.88 * x)
if 3134.41 <= x <= 6101.06 :
 y = x - (0.86 * x)
if x > 6101.06 :
 y = (0.14 * 6101.06)
print("INSS: R$", format(y, ".2f").replace(".", ","))

a = x - y
if a <= 1903.98 :
  z = 0.00
if 1903.99 <= a <= 2826.65 :
  z = (a * 7.5 / 100) - 142.80
if 2826.66 <= a <= 3751.05 :
  z = (a * 15 / 100) - 354.80
if 3751.06 <= a <= 4664.68 :
  z = (a * 22.5 / 100) - 636.13
if a > 4664.68 :
  z = (a * 27.5 / 100) - 869.36
print("IR: R$", format(z, ".2f").replace(".", ","))

l = x - y - z
print("Liquido: R$", format(l, ".2f").replace(".", ","))