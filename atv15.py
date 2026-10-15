#15. Leia um valor inteiro representando o ano de nascimento de uma pessoa e exiba a idade aproximada 
#dela, considerando o ano de referência 2026 (Idade = Ano de referência − Ano de nascimento).
print("Digite o seu ano de nascimento: ")
anoNasc = int(input())
ANO_REF = 2026
idade = ANO_REF - anoNasc
print(f"A sua idade é de: {idade} anos ")