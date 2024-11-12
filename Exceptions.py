def remainder_division(a,b):
    if b == 0:
        # raise ZeroDivisionError
        raise Exception ('Divisor cannot be 0')

    result = a // b
    remainder= a % b
    print(a, '/', b, 'is', result, 'remainder', remainder)

#Main program
remainder_division(10, 0)


#Du kan åpne filer via python og skrive til eller hente fra en fil. 

# file = open ('acronyms.txt') #med denne må du huske på å også lukke filen etter bruk!
#   try:
        #Do file operations here
#       pass
#   finally:
#     file.close()

# with open('acronyms.txt') as file: #Denne vil lukke filen etter at de oppgavene som skal gjøres er fulførte. selv om en exception eller error dukker opp.
        #Do file operations here.

with open('acronyms.txt') as file:
    result = file.read() #Read metoden vil returnere hele filen som en string som default. eller den vil returnere det spesifikke nummer av bytes. 
    print(result)

    #readline metoden returnerer den neste linjen av filen som en string. 
    #readlines metoden returnerer en liste av strings av alle linjene i filen. Du kan da loope gjennom disse slik at du går gjennom hele filen. 

with open('acronyms.txt'):
    result= file.readlines() #Det er også en snarvei med dette hvor du bare kan loope gjennom fil objektet. og dermed trenger du i kke result = file.readlines() 
    for line in result: # Og du kan skrive for line in file: istedet og dette vil gå gjennom hver linje i fil objektet. 
        print(line)

    #Du har forskjellige modes når du åpner en fil. du kan putte with open('textfil', 'w/r/a') men være obs da disse har forskjellige betydninger
            # w is for Write, men denne vil slette filen du allerede har og skrive den på nytt, vær obs på dette dersom du har en fil med masse informasjon.
            # r er for read only, da vil du ikke kunne redigere noe og kunn lese filen.
            # a er for append hvor du da vil kunne legge til noe nytt i filen uten at den informasjonen du har i filen fra før vil endres. 