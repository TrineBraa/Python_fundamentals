temperature = 95

#Du kan skrive en if settning på denne måten hvor elif er else if. 
if temperature > 80:
    print ("It's to hot!")
    print ("Stay inside!")
elif temperature <60:
    print("it's to cold!")
    print ("Stay Inside!")
else:
    print ("Enjoy the outdoors!")

#Du kan også skrive en else if på denne måten dersom det er repetisjon av koden slik du kan se at det er i koden biten over. 
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")


#Logiske operator - and
#begge sammenligningene må være sanne for at if settningen skal være sann.

temp = 75
forecast = "rainy"

if temp < 80 and forecast != "rainly":
    print ("Go outside!")
else:
    print ("Stay inside!")


#En annen måte å gjøre dette på:
#negate means make the opposite: not True => False, not False => True
if not forecast == "rainy":
    print ("Go outside!")
else:
    print("Stay inside!")

#Boolean
raining = False

if raining:
    print ("Stay inside!")

#En annen måte å gjøre dette på:
if not raining: 
    print ("G outside!")
else:
    print ("Stay inside!")