import random
from os import system, name

def clearT():
    if name == "nt":
        _= system("cls")
    else:
        _= system("clear")

figura = [
    """
        ----------
        |        |
        |        O
        |       \\|/
        |        |
        |       / \\
        |
       ===
    """,
    """
        ----------
        |        |
        |        O
        |       \\|/
        |        |
        |       / 
        |
       ===
    """,
    """
        ----------
        |        |
        |        O
        |       \\|/
        |        |
        |       
        |
       ===
    """,
    """
        ----------
        |        |
        |        O
        |       \\|/
        |        
        |       
        |
       ===
    """,
    """
        ----------
        |        |
        |        O
        |       \\|
        |       
        |        
        |
       ===
    """,
        """
        ----------
        |        |
        |        O
        |       \\
        |       
        |        
        |
       ===
    """,
    """
        ----------
        |        |
        |        O
        |       
        |       
        |        
        |
       ===
    """,
        """
        ----------
        |        |
        |        
        |       
        |       
        |        
        |
       ===
    """
        ]

def jogo():
    clearT()
    
    print("\nBem vindo ao jogo da forca!")
    
    while True:
        try:
            cat = int(input("Escolha uma categoria para sua palavra: \n(1) --> Fruta \n(2) --> Animal \n(3) --> Componentes computação\n"))
        except:
            print("Você não escolheu uma categoria, por gentileza, tente novamente")
            continue
        else:
            if cat == 1:
                fruta = ["maçã", "banana", "laranja", "uva", "morango", "limão", "abacaxi", "manga", "melancia", "pera",
          "kiwi", "cereja", "pêssego", "ameixa", "goiaba", "caju", "melão", "jabuticaba", "tangerina", "coco",
          "maracujá", "romã", "framboesa", "amora", "carambola", "lichia", "caqui", "figo", "pitaya", "physalis",
          "açaí", "mirtilo", "atemoia", "jaca", "tamarindo", "graviola"]
                aleat = random.choice(fruta)

            elif cat == 2:
                animal = ["gato", "cachorro", "elefante", "leão", "tigre", "girafa", "urso", "zebra", "rinoceronte", "hipopótamo",
           "gorila", "panda", "cavalo", "vaca", "ovelha", "porco", "galinha", "pato", "ganso", "peru",
           "coelho", "cobra", "tartaruga", "peixe", "golfinho", "baleia", "pinguim", "avestruz", "águia", "gavião",
           "lobo", "raposa", "jaguatirica", "búfalo", "camelo", "esquilo"]
                aleat = random.choice(animal)

            elif cat == 3:
                TI = ["processador", "memoria", "placa-mae", "disco-rigido", "placa-de-video", "fonte-de-alimentacao",
                         "monitor", "teclado", "mouse", "caixa-de-som", "webcam", "microfone", "impressora", "scanner",
                         "roteador", "switch", "hub", "modem", "cabo-de-rede", "wifi", "bluetooth", "webcam", "cartao-de-memoria",
                         "pen-drive", "disco-ssd", "dvd-rom", "bateria", "coolers", "ventoinha", "gabinete", "monitor-touchscreen",
                         "monitor-ultrawide", "monitor-4k", "touchpad", "trackpad"]

                aleat = random.choice(TI)
            break
            
    letras_desc = ["_" for letra in aleat]
    vidas = 7
    letras_error = []
    
    while vidas > 0:
        print("\nVidas restantes: ", vidas)
        print("Letras incorretas", " ".join(letras_error))
        print(figura[vidas])
        print(" ".join(letras_desc))

        tentativa = input("\nDigite uma letra: ").lower()
        
        if tentativa in aleat:
            index = 0

            for letra in aleat:
                if tentativa == letra:
                    letras_desc[index] = letra
                index += 1
        else:
            vidas -= 1
            letras_error.append(tentativa)
        
        if "_" not in letras_desc:
                print("\nParabéns você descobriu a palavra:", aleat)
                break
    if "_" in letras_desc:
        print(figura[vidas])
        print("\nVocê perdeu, a palavra era: ", aleat)
    
if __name__ == "__main__":
    jogo()
    
    