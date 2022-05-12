from random import seed
from random import randint

class Director:
    #
    def __init__(self):
        self.player_score = 300
        self.win_round = ''
        self.continue_playing = ''
        self.cards = self.Cards()
        self.higher_lower = ''

    def get_input(self):
        Director.cards.first_card = Director.cards.get_card()
        Director.cards.second_card = Director.cards.get_card()
        
        print(f"The card is: {Director.cards.first_card}")
        Director.higher_lower = input("Higher or Lower? [H or L] ")

        while (Director.cards.first_card == Director.cards.second_card):
            Director.cards.second_card = Director.cards.get_card()
        
        print(f"The next card is: {Director.cards.second_card}")
        Director.update_score(Director.higher_lower, Director.cards.first_card, Director.cards.second_card)
        print(f"Your score is: {Director.player_score}")
        Director.continue_playing()

    
    def update_score(self, higher_lower, card1, card2):
        if (higher_lower.lower() == "l"):
            if (card1 > card2):
                Director.player_score += 100
            else: 
                Director.player_score -= 75
        elif (higher_lower.lower() == "h"):
            if (card1 < card2):
                Director.player_score += 100
            else: 
                Director.player_score -= 75
        else:
            print("Invalid guess!!!")

    
    def prompt_continue_playing(self):
        Director.continue_playing = input("Would you like to play again? [Y or N] ")

class Cards:

    def __init__(self):
        self.first_card = 0
        self.second_card = 0
    
    def get_card(self):
        return randint(1,14)


def main():
    ''

if __name__ == "__main__":
    main()

''' DESIGN

class: Card

    Responsibility: To hold card values
        first_card: int
        second_card: int

    Behaviors: To get new card values
        flip_first_card(): int
        flip_second_card(): int

class: Director

    Responsibility: To hold player score, win of round, and value of continue play
        player_score: int
        win_round: bool
        continue_playing: bool
    Beaviors: To evaluate card values, update score,
                and prompt for continued play
        
        get_card_info(): int first_card, int second_card
        evaulate_cards_values(): int first_card, int second_card, bool win_round
        update_score(): int score, bool win_round
        prompt_continue_playing(): bool continue_playing
'''