""""
price = input('How much is the burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')
within_budget = float(price) <= 10.00
has_vegetarianoption = vegetarian == 'y'
is_good_choice = within_budget and has_vegetarianoption
if  is_good_choice:
    print("great choice")

if not is_good_choice:
    print("not a great choice")

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'
if  discount_applicable:
    meal_price=meal_price*0.9
    print("discount applied")
else:
    print("no discount")
print("Totalcost:{}".format(meal_price))


oventemp = int(input('How hot is the oven ? '))
if oventemp > 200:
    print('The oven is too hot')
elif oventemp < 150:
    print('The oven is too cold')
elif oventemp==180:
    print('perfect')
else:
    print('That is close enough')

import random
sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)
print('You rolled a {}'.format(random_integer))

import random
def flip_coin():
    coin = random.randint(1, 2)
    if coin == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side
choose = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))
if choose == result:
    print('You win!')
else:
    print('You lose!')"""

import random
def rocksispap():
    hand = random.randint(1, 3)
    if hand == 1:
        side = 'rock'
    elif hand==2:
        side = 'scissors'
    elif hand==3:
        side='paper'
    return side
choose = input('Rock Scissors paper: ').lower()
result = rocksispap().lower()
print('I chose {}'.format(result))
if choose == result:
    print('draw!')
elif choose=='rock' and result=='paper':
    print('You win!')
elif choose == 'rock' and result == 'scissors':
    print('You lose!')
elif choose == 'paper' and result == 'scissors':
    print('You win!')
elif choose == 'paper' and result == 'rock':
    print('You lose!')
elif choose == 'scissors' and result == 'paper':
    print('You lose!')
elif choose == 'scissors' and result == 'rock':
    print('You win!')
else:
    print('You didnt pick correctly')


