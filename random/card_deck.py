card_deck = input().split()
number_of_shuffles = int(input())
final_deck = []

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(card_deck) // 2
    left_side = card_deck[0:middle_of_the_deck]
    right_side = card_deck[middle_of_the_deck::]
    for index in range(len(left_side)):
        final_deck.append(left_side[index])
        final_deck.append(right_side[index])
    card_deck = final_deck
print(card_deck)