#10.  Peça  a  leitura  do  nome  de  um  produto  (texto)  e  do  seu  preço  (número  decimal),  e  exiba  as  duas 
#informações formatadas em uma única linha, como "Produto: [nome] – Preço: R$ [preço]
print("Digite o nome de um produto, e logo após, digite o valor do mesmo")
nome = input()
preco = float(input())
print(f"O produto escolhido foi: {nome} e seu preço é de: R$ {preco:.2f}")