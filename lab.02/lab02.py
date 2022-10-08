###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Luis Paulo Siqueira Silva
# RA: 183045
###################################################

x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

a = (x / v_1) - (t / 60)
b = x / v_2

if a < b :
 print("True")
else :
 print("False")