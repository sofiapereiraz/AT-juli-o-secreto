import random
print("advinhe o numero entre 1 e 100")
numero_secreto=random.randint(1,100)
tentativas=0
acertou=False
while not acertou:
    chute=int(input("digite seu palpite: "))
    tentativas+=1
    if chute == numero_secreto:
        print(f"voce acertou em {tentativas} tentativas.")
        acertou=True
    elif chute > numero_secreto:
        print(f"chute foi maior que o numero")

    elif chute < numero_secreto:
        print(f"chute foi menor que o numero secreto")
        