from random import seed
from random import randint

class Director:

    def __init__(self):
        self.player_score = 300
        self.win_round = ''
        self.continue_playing = True
        self.cards = Cards()
        self.higher_lower = ''

    def get_input(self):
        
        print(f"The card is: {self.cards.first_card}")
        self.higher_lower = input("Higher or Lower? [H or L] ")

        while (self.cards.first_card == self.cards.second_card):
            self.cards.second_card = self.cards.get_card()
        
        print(f"The next card is: {self.cards.second_card}")
        self.update_score(self.higher_lower, self.cards.first_card, self.cards.second_card)
        print(f"Your score is: {self.player_score}")
        self.prompt_continue_playing()

    
    def update_score(self, higher_lower, card1, card2):
        if (higher_lower.lower() == "l"):
            if (card1 > card2):
                self.player_score += 100
            else: 
                self.player_score -= 75
        elif (higher_lower.lower() == "h"):
            if (card1 < card2):
                self.player_score += 100
            else: 
                self.player_score -= 75
        else:
            print("Invalid guess!!!")
    
    def prompt_continue_playing(self):
        play = input("Would you like to play again? [Y or N] ")
        if play.lower() == 'n':
            print ("Thanks for playing!")
            self.continue_playing == False
            quit()

        

class Cards:
    
    def __init__(self):
        self.first_card = randint(1,13)
        self.second_card = randint(1,13)
    
    def get_card(self):
        seed(0)
        return randint(1,13)


def main():
    director = Director()
    while (director.continue_playing):
        
        director.get_input()

if __name__ == "__main__":
    main()