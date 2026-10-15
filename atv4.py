#4. Peça a leitura de um número decimal representando o preço de um produto e exiba o valor formatado 
#com duas casas decimais, precedido do símbolo "R$". 
print("Digite o preço de um produto: ")
preco = float(input()) 
#colocar o valor entre chaves e :.2f faz o valor da variavel retornar como número decimal de duas casas
#f após o parenteses do print permite acrescentar variáveis entre as chaves
print(f"O preço desse produto é: R$ {preco:.2f}")