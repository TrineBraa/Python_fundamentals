#Når du lager en classe i Python gjør du det på denne måten

class Robot_Dog:
    #Denne funksjonen lar os initialisere klassens properties. self er altid det første parametret og referer til instansen av klassen vi lager eller det nåværende objektet
    #Du sender også inn parametre du ønsker å initialisere med klassen og objektet du lager
    def __init__ (self, name_val, breed_val): #Disse kan enten ha det samme navnet som objektets properties eller du kan gi de sendte parametrene et annen navn for å ikke forvirre deg selv. 
        self.name = name_val
        self.breed = breed_val

    def bark(self):
        print('Woof Woof!')

#Main program
my_dog = Robot_Dog('Spot', 'Chihuaha')
print (my_dog.name)
print (my_dog.breed)

my_dog.bark()

#Demo at company.py and Employee.py

#Class Inheritance
#Has-a slik som eksemplet over, en arbeids plass har ansatte( A company has empoyees), A robot has a Battery
#Is-a mer spesifikt, en robot hun er en robot klasse, en robot katt er en robot. 

#Parent class
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)

    def eat(self):
        print("I'm hungry!")

#Child class
class Dog_Robot(Robot): #Du setter klassen denne arver fra i parantes. dersom du ikke har en init metode her vil den automatisk kalle forelderen's init metode. 
    def make_noise(self):
        print('Woof Woof!')

    def eat(self):
        super().eat()
        print('I like bacon!')

my_robot_dog = Dog_Robot('Bud')
my_robot_dog.walk(10) #Du kan kalle alle metoder knyttet til enten robot eller robot hund. 
my_robot_dog.make_noise()
my_robot_dog.eat()

#Det er veldig sømløse kall til metoder fra de to klassene når arv er brukt. Du kan kalle metoder fra både foreldre og barne klassen. 
#Method overriding: Dersom du har en eat i dette tilfellet i robot klassen som printer 'I'm hungry' 
# Denne vil printes med mindre du overkjører denne og lager en helt lik metode i hunden, da vil denne bli kjørt for alle hunde robotene du lager i prosjektet. 
# Men dersom du også ønsker å kjøre metoden fra foreldre klassen kan du bruke noe som heter Super som er en metode som gir deg tillgang til foreldre metoden også. 

#Demo i videre utforming av employee og Company filene!