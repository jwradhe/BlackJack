from random import randint
import time

class BlackJack:

    def __init__(self):
        self.user_pts = 0
        self.computer_pts = 0

    # Funktion för randomkort värde 1-10
    def card(self):
        return randint(1, 10)

    # Starta spelet, få 2 kort var
    def start(self, player):
        card1 = self.card()
        card2 = self.card()
        val = card1 + card2
        if player == 'user':
            self.user_pts += val
            print(f'Användare startkort: {card1}+{card2}. totalt: {val}')
        elif player == 'computer':
            self.computer_pts += val
            print(f'Dators ena startkort: {card1}')

    # Fortsätta spelet, få ett kort i taget
    def play(self, player):
        if player == "user":
            val = self.card()
            self.user_pts += val
            print(f'Du fick {val}, totalt {self.user_pts}')
            if self.user_pts > 21:
                print("Du fick över 21, game over")
                return "end"
        elif player == "computer":
            while True:
                if self.computer_pts < 17:
                    time.sleep(1)
                    val = self.card()
                    self.computer_pts += val
                    print(f'Datorn fick {val} denna omgång, totalt {self.computer_pts}')
                    time.sleep(1)
                    if self.computer_pts > 21:
                        print("Datorn fick över 21, du vann")
                        return "win"
                else:
                    print(f'Datorn har {self.computer_pts}, men väljer att stanna.')
                    time.sleep(1)
                    return 'stop'
        return None

    # När spelet stoppats och ingen förlorat så kollas resultatet för vinnare.
    def checkWinner(self):
        if self.user_pts == self.computer_pts:
            print(f'Du har {self.user_pts} och datorn har {self.computer_pts}, matchen är oavgjord!')
        elif self.user_pts > self.computer_pts:
            print(f'Du har {self.user_pts} och datorn har {self.computer_pts}, du vann!')
        elif self.computer_pts > self.user_pts:
            print(f'Du har {self.user_pts} och datorn har {self.computer_pts}, datorn vann!')
    

def main():

    game = BlackJack()

    while True:
        try:

            # Få startkort
            if(game.user_pts == 0):
                game.start('computer')
                game.start('user')
   
            # Vill användaren fortsätta
            user = input("Fortsätta? (hit/stand): ").lower()

            # Ja = fortsätta tills man går över 21
            if user == 'hit':
                result = game.play('user')
                if result == "end":
                    break  

            # Nej, man stannar och datorns tur  
            elif user == 'stand': 
                result = game.play('computer')
                if result == "win":
                    break  
                elif result == "stop":
                    game.checkWinner()
                    break

            # Om varken hit eller stand resultat.
            elif user != 'hit' or user != 'stand':
                print("Felaktigt svar, försök igen!")
                continue
            else:
                break  

        except ValueError:
            print('Nu blev det nog lite fel här!')


if __name__ == "__main__":
    main()        