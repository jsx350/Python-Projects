#Jonathan Stanley CIS156

#Prompts the user to enter the starting values for number and increasing percent
number = int(input('Enter the starting number of organisims: '))
increasing_percentage = int(input('Enter the average daily increase: '))

#Prompts the user to enter the number of days
days = int(input('Enter the number of days: '))

#Displays the header of the following table
print('Days Approximate \tPopulation')

#Displays the values for the days and population and calculates the increasing percentage
for x in range(1, days+1):
    if x > 1:
        increase = number * increasing_percentage /100
        number += increase
        
    print(x,'\t\t\t',format(number, '.2f'))
