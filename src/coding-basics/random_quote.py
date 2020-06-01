#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script flow and debugging. Print your own quote!"""

import random

QUOTES = [
    "I see a DevNet Certification coming soon.",
    "All promises are either broken or kept. Or rejected.",
    "If you lose your temper, don't go looking for it.",
]

def generate_quote() -> str:
    """Use a random selection to choose a random quote from the list."""
    return random.choice(QUOTES)

def generate_lucky_numbers(how_many: int) -> list:
    """Returns a list of (random) 'lucky' numbers."""
    lucky_numbers = []
    for _ in range(how_many):
        lucky_numbers.append(random.randint(0, 99))
    return lucky_numbers

def create_random_quote(how_many_lucky_numbers: int) -> str:
    """Create and return a random quote.

    The message should include the user's quote and lucky numbers.
    """
    # TRYIT: Create a random quote by calling generate_quote() and
    # generate_lucky_numbers() and then composing and returning the quote.


    )

def main():
    """Create and print a quote."""
    print("Get your quote!")

    # Prompt the user for how many lucky numbers they would like
    qty_lucky_numbers = input("Also, how many lucky numbers would you like?  ")
    qty_lucky_numbers = int(qty_lucky_numbers.strip())

    # Create and display the response
    random_quote = create_random_quote(qty_lucky_numbers)
    print("\nHere is your quote:\n")
    print(random_quote)

if __name__ == '__main__':
    main()
