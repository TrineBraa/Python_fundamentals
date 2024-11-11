expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(expenses)
sum2 = 0

for x in expenses:
    sum2 = sum2 + x
    print ('You spent $', sum2, sep='')

#sep står for seperator, og vi setter denne for uten den vil du ha et extra mellomrom mellom $ og totalen. 
print('You spent a total of $', total, sep='')

#Endring ved å bruke range og dermed gjøre at brukeren kan inputte egne valg.

total2= 0
expenses2 = []
for i in range(7):
    expenses2.append(float(input("Enter an expense:")))

total2 = sum(expenses2)

print("you spent $", total2, sep='')

#Dersom brukeren ikke har 7 inputs kan du lagre en input til en variabel og heller bruke variabelen til range callet. eks.
num_expenses= int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses2.append(float(input("Enter an Expense:")))