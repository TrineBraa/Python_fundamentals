print("hello World!")

# Du kan kalle på en int funksjon og gjøre om en desimal til en int
amount = int (10.6)
amount
10

# Her kaller du på en float funksjon som vil gjøre om int til en desimal
amount = float(10)
amount
10.0

# Alt som er innenfor '' eller "" kalles for text eller string i Python. Dersom du skal ha en appostrof i stringen gir det menig å bruke "" når du setter opp string. 
name = 'Trine'

# Du kan også sette strings sammen ved å bruke + Du må også legge inn mellomrom ellers blir de to tekstene satt sammen. 
hello = "hello"
name = "Trine"
greeting = hello + " " + name
print (greeting)

hello2 = "Hello there "
# Dette er en variablen hvor den vil lagre input fra brukeren. 
my_name = input("what's your name?\n")
# Denne printe teksten på skjermen og vente på et input og enter press før den går videre. 

print (hello2 + my_name)