#8. Peça a leitura da quantidade de itens comprados (número inteiro) e do valor unitário do item (número 
#decimal), calcule e exiba o valor total da compra. 
print("Digite a quantidade desse item que você comprou, e logo após isso, o valor desse item: ")
qtdItem = int(input())
vlrItem = float(input())
vlrTotal = qtdItem *vlrItem
print(f"O valor total da sua compra foi de: {vlrTotal:.2f}")