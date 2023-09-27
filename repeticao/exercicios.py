# Fácil  1 – Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
# numero = int(input("Digite um numero pra ser calculada a tabuada: "))

# contador = 0
# while contador < 10:
#     print(f"{numero} * {contador} = {numero * contador}")
#     contador += 1

# Fácil  2 –  Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.
# Use um loop for externo para iterar de 1 a 10
# for numero in range(1, 11):
#     print(f"Tabuada do {numero}:")

#     for j in range(1, 11):
#         resultado = numero * j
#         print(f"{numero} * {j} = {resultado}")

#  Faça um programa que verifique e mostre os números entre 1.000 e 2.000
#  (inclusive) que, quando divididos por 11 produzam resto igual a 2.
# numeros = []
# for i in range(1000, 2001):
#     if i % 11 == 2:
#         numeros.append(i)
#         print(i)

# Dificil 4
# n = int(input("Digite um valor inteiro e positivo n: "))

# if n <= 0:
#     print("O valor de n deve ser inteiro e positivo.")
# else:
#     soma = 0.0
#     for i in range(1, n + 1):
#         soma += 1.0 / i

#     print(f"A soma da série é: {soma}")



# Intermediário 5 – Faça um programa que leia três valores (A, B, C)
#  e mostre-os na ordem lida.  Em seguida, mostre-os em
# ordem crescente e decrescente.
# lista_valores = []
# for i in range(3):
#     valor = float(input("Digite o valor"))
#     lista_valores.append(valor)

# print("Ordem lida")
# for i in lista_valores:
#     print(i)

# lista_valores_crescente = sorted(lista_valores)
# print("Ordem crescente")
# for i in lista_valores_crescente:
#     print(i)

# lista_valores_descrescente = sorted(lista_valores, reverse=True)

# print("Ordem decrescente")
# for i in lista_valores_descrescente:
#     print(i)


# Fácil 6 –   Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).  Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

# Inicialize o faturamento total como 0
faturamento_total = 0

# Solicite os faturamentos dos 5 clientes
for i in range(1, 6):
    faturamento_cliente = float(input(f"Digite o faturamento do cliente {i}: R$ "))
    faturamento_total += faturamento_cliente

# Verifique se o faturamento total foi superior a R$ 54.000
if faturamento_total > 54000:
    superavit = faturamento_total - 54000
    print(f"O faturamento total foi superior em R$ {superavit:.2f} a loja B (R$ 54.000).")
else:
    print("O faturamento total não foi superior a loja B (R$ 54.000).")


# # Atividade
# while True:
#     print("Menu de opções:")
#     print("1. Novo salário")
#     print("2. Férias")
#     print("3. Décimo terceiro")
#     print("4. Sair")
#     opcao = int(input("Digite a opção desejada: "))

#     if opcao == 1:
#         salario = float(input("Digite o salário do funcionário: "))
#         if salario <= 350:
#             novo_salario = salario + (salario * 0.15)
#         elif salario <= 600:
#             novo_salario = salario + (salario * 0.10)
#         else:
#             novo_salario = salario + (salario * 0.05)
#         print("Novo salário: R$", novo_salario)
#     elif opcao == 2:
#         salario = float(input("Digite o salário do funcionário: "))
#         ferias = salario + (salario / 3)
#         print("Valor das férias: R$", ferias)
#     elif opcao == 3:
#         salario = float(input("Digite o salário do funcionário: "))
#         meses_trabalhados = int(input("Digite o número de meses trabalhados: "))
#         decimo_terceiro = salario * meses_trabalhados / 12
#         print("Valor do décimo terceiro: R$", decimo_terceiro)
#     elif opcao == 4:
#         print("Programa encerrado.")
#         break
#     else:
#         print("Opção inválida. Digite uma opção válida.")