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
        self.first_card = ''
        self.second_card = 0
    
    def flip_first_card(self):
        ''
    
<<<<<<< HEAD
    def flip_second_card(self):
=======
    def get_card(self):
>>>>>>> 211144ca85acbb4238637dbcd8639538324d3cfa
        ''


''' DESIGN
<<<<<<< HEAD
class: Card
    Responsibility: To hold card values
        first_card: int
        second_card: int
    Behaviors: To get new card values
        flip_first_card(): int
        flip_second_card(): int
class: Director
=======

class: Card

    Responsibility: To hold card values
        first_card: int
        second_card: int

    Behaviors: To get new card values
        flip_first_card(): int
        flip_second_card(): int

class: Director

>>>>>>> 211144ca85acbb4238637dbcd8639538324d3cfa
    Responsibility: To hold player score, win of round, and value of continue play
        player_score: int
        win_round: bool
        continue_playing: bool
<<<<<<< HEAD
=======

>>>>>>> 211144ca85acbb4238637dbcd8639538324d3cfa
    Beaviors: To evaluate card values, update score,
                and prompt for continued play
        
        get_card_info(): int first_card, int second_card
        evaulate_cards_values(): int first_card, int second_card, bool win_round
        update_score(): int score, bool win_round
        prompt_continue_playing(): bool continue_playing
'''