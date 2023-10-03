
# palavra = "python"
from palavra_forca import palavraj
letra_usuario = []
chances = 4
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letra_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chancesi")
    tentativa = input("Escolha uma letra: ")
    letra_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

        ganhou = True
        for letra in palavra:
            if letra.lower() not in letra_usuario:
                ganhou = False

    if chances == 0 or ganhou:

     break
   
    if ganhou:
        print(f"Parabens, você ganhou. A palavra era: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")