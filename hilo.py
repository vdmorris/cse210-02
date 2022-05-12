from random import seed
from random import randint

class Director:

    def get_input():
        cards = Cards
        higher_lower = " "
        first_card = cards.get_card()
        second_card = cards.get_card()
        
        print(f"The card is: {first_card}")
        higher_lower = input("Higher or Lower? [H or L] ")

        while (first_card == second_card):
            return second_card
        
        print(f"The next card is: {second_card}")

    
    def update_score():
        ''
    
    def prompt_repeat():
        ''

class Cards:

    
    def get_card():
        card = randint(1,14)
        return card


def main():
    card = Cards
    director = Director
    found = False
    while not found:
        print ("***HiLo Game***")
        guess = int(input("What is your guess?"))
        if guess == target:
            print("Good guess, you found it!")
            repeat = input("Play again? y/n")
            if repeat == 'n':
                found = True
            elif repeat == 'y':
                target = rand.randint(1,100)
                found = False
        else:
            if guess < target:
                print("too low")
            else:
                print("too high")

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