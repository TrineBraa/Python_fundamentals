breakfast =['Egg Sandwich', 'Bagel', 'Coffee']
lunch = ['BLT', 'PB&J', 'Turkey Sandwich']
dinner= ['Soup', 'Salad', 'Spaghetti', 'Taco']

menus= [['Egg Sandwich', 'Bagel', 'Coffee'],
        ['BLT', 'PB&J', 'Turkey Sandwich'],
        ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print('Breakfast Menu:\t', menus[0])
print('Lunch Manu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

#For å nå kunne nå f.eks. Bagel i den første menyen vil du kunne gjøre det på denne måten
print (menus[0][1])

#Du kan også bruke en dictinary for dette

menus2 = {'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus2['Breakfast'])
print('Lunch Manu:\t', menus2['Lunch'])
print('Dinner Menu:\t', menus2['Dinner'])

#Dersom du bruker dette med en for loop vil du kunn få nøkkelen i return, Breakfast, Lunch og Dinner. Men dersom du ønsker mer gjør du dette på denne måten:
for name, menu in menus2.items():
    print(name, ':', menu)


#Du kan også bruke Dictionaries til å representere objekter.
person = {'Name' : 'Sarah Smith',
          'City' : 'Orlando',
          'Age' : '86'}

print (person.get('Name'), 'is', person.get('Age'), 'years old.')

#Videre eks med demo: contacts.py
#Annet eks i space.py