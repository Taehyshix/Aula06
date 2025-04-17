repeticao = "S"
while repeticao == "S" or "s":
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura * altura)

    if imc <= 18.5:
        print("Abaixo do peso.")
    elif imc >= 18.6 and imc < 24.9:
        print("Peso ideal, parabéns!")
    elif imc >= 25.0 and imc < 29.9 :
        print("Levente acima do peso.")
    elif imc >= 30.0 and imc < 34.9:
        print("Obesidade grau I")
    elif imc >= 35.0 and imc < 39.9:
        print("Obesidade grau II (severa)")
    else:
        print("Obesidade grau III (mórbida)")
    repeticao = input("Aperte S para continuar ou qualquer tecla para parar.")
print("Fim")