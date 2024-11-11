#Tom liste:
empty = []

#Liste med strings
words= ['idk', 'tbh', 'brb']

#liste med tall
nums = [5, 10, 15]

#liste av forskjellige ting
mixed = [ 5, 'idk', 1.5]

#Liste av lister
lists= [['a', 'b', 'c'], ['d', 'e', 'f']]

#              0    1       2       3
acronyms = ['LOL', 'IDK', 'SMH', 'TBH']

print (acronyms[2])

acro = []

acro.append('LOL')
acro.append('SMH')
# acro er listen du vil endre, dot, metode navnet, hva du ønsker å legge til listen i paranteser. 

acro.remove('SMH') 
#OR
#del acro [1]

print (acro)

# if: 1 (item), in list [1, 2, 3, 4, 5]
if 1 in [1, 2, 3, 4, 5]:
    print('True')


acronyms2 = ['LOL', 'IDK', 'SMH', 'TBH']
word = 'BFN'

if word in acronyms2:
    print (word + ' is in the list')
else:
    print (word + ' is NOT in the list')

#for loop
#for, acronym er variabelen i listen som du kan gi valgfritt navn til, in, acronyms er listen vi ønsker å gå gjennom. 
for acronym in acronyms:
    print (acronym)


#Loops med Range
range(7) #Denne returnerer en range av 7 integers (1, 2, 3, 4, 5, 6)
range(0, 7, 1) #Du gan gi range en start, stop og step verdi
range (2, 14, 2) # denne vil gi oss partall fra 2 til 14 med 2 i økning. 

for i in range(7):
    print(i)

#Load_calculator er et eksempel på bruk av range i forloops.


#Dictionaries map keys to values
acronyms3 = {'LOL' : 'Laugh out loud',
             'IDK' : "I don't know",
             'TBH' : 'To be honest'}
print(acronyms3['LOL'])
#Dictionaries kan holde hva enn du ønsker. Strings to strings, strings to numbers. eller en samling av flere forskjellige.
Acronym = {'LOL' : 'laugh out loud'}
menu = {'Soup' : 5}
my_dict = {10: 'hello',
            2: 6.5}

#Du kan legge ting til et dictionary:
Acronym_eks = {}
Acronym_eks['LOL'] = 'Laugh out loud' #Det i brackets er nøkkelen og verdien settes bak erlik tegnet. Du kan bruke samme metoden for å oppdatere en verdi. Dersom nøkkelen er der vil den oppdateres. 
#For å slette vil du bruke nøkkelordet del, eks: del.Acronym_eks['LOL]
#Dersom du prøver å nå en nøkkel som ikke er der vil få en Key error
#Ved å bruke Get vil du ikke kræsje programmet men du vil heller få en retur som sier non om nøkkelen ikke eksisterer. 

sentence= 'IDK' + ' what happened ' + 'TBH'
translation = acronyms3.get('IDK') +' what happened '+ acronyms3.get('TBH') #denne vil bruke akronymene som er nøkklene til å gi deg verdien som er settningen. 
print('sentence:', sentence)
print('translation:', translation)

#movie_schedule er et eksempel på bruk av dictionaries.