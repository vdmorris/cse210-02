from random import seed
from random import randint

class Director:
    #
    def __init__(self):
        card = self.Cards
        self.player_score = 300
        self.win_round = ''
        self.continue_playing = ''
    
    def get_card_info(self):
        ''
    
    def evaulate_cards_values(self):
        ''
    
    def update_score(self):
        ''
    
    def prompt_continue_playing(self):
        ''

class Cards:

    def __init__(self):
        pass
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