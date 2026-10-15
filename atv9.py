#9. Leia um valor decimal representando uma temperatura em graus Celsius e exiba a mesma 
#temperatura convertida para Fahrenheit.
print("Digite a temperatura em Celsius")
tempCelsius = float(input())
conversorCelpFah = (tempCelsius * 9/5) + 32
print(f"A temperatura informada em Celsius convertida para Fahrenheit é de: {conversorCelpFah:.2f} °F")