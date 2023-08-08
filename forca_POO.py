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

class JogoForca():

    def __innit__(self, palavra):
        self.palavra = palavra
        self.l_errada = []
        self.l_certa = []

    def letras(self, letra):
        if letra in self.palavra and letra not in self.l_certa:
           self.l_certa.append(letra)
        elif letra not in self.palavra and letra not in self.l_errada:
            self.l_errada.append(letra)
        else:
            return False
        return True 

    def Game_over(self):
        return self.game_on() or (len(self.l_errada) == 6)
    
    def Game_on(self):
        if '_' not in self.letra_palavra():
            return True
        return False
    
    def letra_palavra(self): 
        rtn = ''
        for letra in self.palavra:
            if letra not in self.l_certa:
                rtn += '_'
            else:
                rtn += letra
    
    def exibicao(self):
        print(figura[len(self.l_errada)])
        print('\nPalavra ' + self.letra_palavra())
        print('\nLetras erradas: ',)
        for letra in self.l_errada:
            print(letra,)
        print()
        print('Letras corretas: ',)
        for letra in self.l_certa:
            print(letra,)
        print()

def sort_palavra():
    palavras = ['uva','maca','banana']
    palavra = random.choice(palavras)
    return palavra
    
def main():
    clearT()
    game = JogoForca(sort_palavra())
    while not game.Game_over():
        game.exibicao()
        user = input('\nDigite uma letra: ')
        game.letras(user)
    game.exibicao()

    if game.Game_on():
        print('\nParabens você venceu')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era '+ game.palavra)

if __name__ == "__main__":
    main()