#Faça um algoritmo para receber um níumero qualquer e imprimir na tela se o número é par ou ímpar,
# positivo ou negativo

num = int(input("Digite um número: "))
if num % 2 == 0 and num < 0:
    print(f"{num} par e negativo")
elif num == 0 and num >= 0:
    print(f"{num} impar e positivo")
elif num != 0 and num < 0:
    print(f"Seu número {num} é impar e negativo")
else:
    print(f"Seu {num} é impar e positivo")