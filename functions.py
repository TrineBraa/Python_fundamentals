import random
#Functions are mini programs that complete a spesific task. 

print('Hello world')

#name = input('Enter your name:\n')

amount = int (10.6)

roll = random.randint(1,6)

#Definere en funksjon
#obs med scoping igjen. I dette tilfellet vil variabelen name kunn være tilgjengelig for greeting funksjonen. 
def greeting(name):
    print('hello', name)

#Obs på indentations. Dersom disse er tabbet inn vil de ikke kjøre fordi de telles som en del av greetings funksjonen.
input_name = input('Enter your name:\n')

greeting(input_name)

    #En funksjon må defineres først før du kan kalle på den. Du må dermed lage funksjonene først også lage kall og lignende under. 

def addition(a, b):
    return a + b

def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2= float(input('enter your 2nd number:\n'))

    result = addition(num1, num2)
    print('The result is:', result)

main()

#Ny Demo i dice_game.py
