import random

class Director:
    
    def get_card_info():
        card1 = Cards.flip_first_card()
        
    
    def evaulate_cards_values():
        ''
    
    def update_score():
        score = 300


        return score
    
    def prompt_continue_playing():
        ''

class Cards:
    
    def flip_first_card():
        ''
    
    def flip_second_card():
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