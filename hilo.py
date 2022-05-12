from random import seed
from random import randint
class Director:
    #
    def __init__(self):
        card = self.Cards
    
    def get_input(self):
        ''
    
    def update(self):
        ''
    
    def do_output(self):
        ''
    
    def start_game(self):
        ''

class Cards:

    def __init__(self):
        pass
    
    def get_card(self):
<<<<<<< HEAD
        return randint(1,14)


def main():
    ''

if __name__ == "__main__":
    main()
=======
        ''


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
>>>>>>> 211144ca85acbb4238637dbcd8639538324d3cfa
