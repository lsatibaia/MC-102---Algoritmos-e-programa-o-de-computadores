###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
###################################################

ryu = int(input())
ken = int(input())
a = int(input())
x = 0
y = 0
b = ken
c = ryu

while b > 0 and c > 0:
 if a > 0:
   print("RYU APLICOU UM GOLPE:" , a)
   b = ken - a
   if b < 0:
      b = 0
   print("HP RYU =" , ryu)
   print("HP KEN =" , b)
   x = x + 1
   ken = b
 if a < 0:
   c = ryu + a
   if c < 0:
      c = 0
   print("KEN APLICOU UM GOLPE:" , (-1 * a))
   print("HP RYU =" , c)
   print("HP KEN =" , ken)
   y = y + 1
   ryu = c
 if b <= 0 or c <= 0: 
   break
 a = int(input())
 

if b > 0 and c <= 0: 
 print("LUTADOR VENCEDOR: KEN")
if b <= 0 and c > 0:
 print("LUTADOR VENCEDOR: RYU")
print("GOLPES RYU =" , x)
print("GOLPES KEN =" , y)