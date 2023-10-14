import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
especial = "!@#%&*()+={}[]?/:;><.,-_"

upperq = input ("Letras Maisculas?(S/N): ")
lowerq = input ("Letras Minusculas?(S/N): ")
numq = input ("Numeros?(S/N): ")
especq = input ("Caracteres Especiais?(S/N): ")

afirmativo = ["Sim","SIM","S","sim","s"]

if upperq in afirmativo:
    upper = True
else:
    upper = False 

if lowerq in afirmativo:
    lower = True
else:
    lower = False 

if numq in afirmativo:
    num = True
else:
    num = False 

if especq in afirmativo:
    espec = True
else:
    espec = False 

all = ""

if upper:
    all += uppercase
if lower:
    all += lowercase
if num:
    all += numbers
if espec:
    all += especial

print (all)

lenght = int(input("Tamanho Da Senha?: "))
amount = int(input("Quantas Senhas Serao Geradas?: "))

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)