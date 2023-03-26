"""with open('people.txt', 'w') as text_file:
    people = 'Joanne \nSusan \nAmina'
    text_file.write(people)
with open('people.txt', 'r') as text_file:
    contents = text_file.read()
print(contents)

with open('todo.txt','w')  as text_file:
    todo='shopping\ncooking'
    text_file.write(todo)

newtodo = input('Enter a to-do item: ')
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()
    todo = todo + '\n'+ newtodo + '\n'
with open('todo.txt', 'w') as todo_file:
    todo_file.write(todo)
    print(todo)

import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)
shortest_height = min(heights)
print(shortest_height)"""

