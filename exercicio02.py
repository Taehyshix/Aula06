#Faça um algoritmo para receber um níumero qualquer e imprimir na tela se o número é par ou ímpar,
#positivo ou negativo.

repetir = "S"

while repetir == "S" or repetir == "s":
    num = int(input("Digite um número: "))
    if num % 2 == 0 and num < 0:
        print(f"{num} par e negativo")
    elif num == 0 and num >= 0:
        print(f"{num} impar e positivo")
    elif num != 0 and num < 0:
        print(f"Seu número {num} é impar e negativo")
    else:
        print(f"Seu {num} é impar e positivo")
    repetir = input("Digite S para continuar po qualquer tecla para parar")
print("Programa finalizado!")

"""
Resolução:
num = int(input("Digite um numero: "))
if num >0:
    if num%2==0:
        print("Par é positivo")
    else:
        print("impar e positivo")
else:
    if num % 2 ==0:
        print("par e negativo")
    else:
        print("impar e negativo")
        """