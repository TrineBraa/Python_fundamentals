# obs inputs vil alltid tas inn som strings, så de må converters dersom du skal ha tall inn.
# age = input ("how old are you ?\n")

# eks på dette:
age = int(input("How old are you? \n"))

# Denne vil gi et desimal tall og dersom du ønsker fulle tall er det en måte å gjøre det på 
# decades = age/10

decades = age // 10
years = age % 10 
# Prosent tegnet eller modulus tar det som er igjen å setter det som et eget tall

# Denne vil også gi en error siden den ikke kan lese en float i en string så denne må converteres til en string. 
# print ("You are " + decades + " decades old.")

print ("You are " + str(decades) + " decades and " + str(years) + " years old.")