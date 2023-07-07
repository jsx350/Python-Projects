#Imports the random tool
import random
#Defines the function for writing the file
def write():
    object_file = open('random_numbers.txt', 'w')
    how_many = int(input('Enter a number as an integer for how many random numbers '
                          'the file will hold: '))
#Defines the range of numbers and which files to write them to
    for i in range(how_many):
        number = random.randrange(1, 501)
        number = str(number)
        object_file.write(number)
        object_file.write('\n')
    object_file.close()
write()