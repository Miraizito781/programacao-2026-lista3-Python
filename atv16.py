#16. Peça a leitura de dois números inteiros representando horas e minutos e exiba a quantidade total de 
#minutos correspondente a essa duração (Total de minutos = horas × 60 + minutos)
print("Digite a hora e logo após, os minutos: ")
horas = int(input())
minutos = int(input())
totalMin = (horas * 60) + minutos
print(f"O total de minutos no horário informado é de: {totalMin} minutos")