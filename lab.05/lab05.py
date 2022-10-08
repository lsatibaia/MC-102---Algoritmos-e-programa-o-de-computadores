###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
###################################################

n1 = int(input())
n3 = int(input())
n4 = int(input())
n6 =int(input())

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))
print("Lista de apostas:")


for n2 in range(n1+1, n3) :
  for n5 in range(n4+1, n6) :
   if n1 % 2 == 0 and n2 % 2 == 0 :
     continue
   if n1 % 2 == 1 and n2 % 2 == 1 :
     continue
   if n1 % 2 == 0 and n5 % 2 == 1 :
      continue
   if n1 % 2 == 1 and n5 % 2 == 0 :
     continue
   if (n1 + n2 + n3 + n4 + n5 + n6) % 13 == 0 :
     continue
   if (n1 + n2 + n3 + n4 + n5 + n6) % 7 == 0 :
     continue
   print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))