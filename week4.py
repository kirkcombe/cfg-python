"""carrots = int(input('How many carrots do you have? '))
rabbits = 6
if rabbits> carrots:
    print('There are not enough carrots')
elif rabbits <carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')

clothes = [
    "shorts",
    "shoes",
    "t-shirt",]
if clothes[0] =="shorts":
    clothes[0]="warm coat"
    print (clothes)

scores = [13, 3, 23, 45, 49, 8,12,13,99,200]
print('Number of scores {}'.format(len(scores)))
print('Highest score {}'.format(max(scores)))
print('Lowest score {}'.format(min(scores)))

ShoppingList=["bread","cake","eggs"]
if "bread" in  ShoppingList:
    ShoppingList.append('butter')
print(ShoppingList)

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0
for cost in costs:
    total_cost = cost+total_cost
print(round(total_cost,2))

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
    'longitude': 127,
    'latitude': 63,
    }
}
print(place['name'])
print(place['post_code'])
print(place['street_number'])
print(place['location']['longitude'])


fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for fruit in fruits:
    print(fruit["name"])
    print(fruit["colour"])
    print(fruit["price"])
"""
import random
First_name = ['Ben', 'sam', 'Sue']
Surname=['smith', 'brown','Wright']
Name= random.choice(First_name)+" "+random.choice(Surname)
print(Name)