"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    number = [number, number+1, number+2]
    for item in number:
        if item < 0:
            number.remove(item)
    return number

print(get_rounds(5))



def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2

print(concatenate_rounds([1, 2, 3], [4, 5, 6]))



def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False

print(list_contains_round([1, 2, 3, 4, 5], 2))
print(list_contains_round([1, 2, 3, 4, 5], 7))



def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)

print(card_average([5, 6, 7, 8, 9]))



def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average_first_last = (hand[0] + hand[-1]) / 2
    middle_index = len(hand) // 2
    middle_card = hand[middle_index]
    true_average = sum(hand) / len(hand)
    return average_first_last == true_average or middle_card == true_average

print(approx_average_is_average([1,2,3]))
print(approx_average_is_average([2,3,4,8,8]))
print(approx_average_is_average([1,2,3,5,9]))



def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_positions = hand[0::2]
    odd_positions = hand[1::2]
    average_evens = sum(even_positions) / len(even_positions)
    average_odds = sum(odd_positions) / len(odd_positions)
    
    if average_evens == average_odds:
        return True
    else:
        return False

print(average_even_is_average_odd([1,2,3]))
print(average_even_is_average_odd([1,3,2,4]))



def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    jack_value = 11

    if hand[-1] == jack_value:
        hand[-1] = jack_value * 2
    else:
        hand[-1] = hand[-1]
    return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))