#Jonathan Stanley CIS156
#This program asks the user a series of questions in order to troubleshoot router issues.
#If the user responds "Y" at any point the program ends.

#Informs the user to use Y or N in place of yes or no responses
print('Reboot the computer and try to connect.\n(Y/N) Enter Y for yes or N for no.')

#Prompts the user to enter if the solution worked, this repeats for all steps.
user_answer = input('Did that fix the problem? ')

##If the user responds no, the next step is displayed, this repeats for all steps.
if user_answer == 'Y' or user_answer == 'N':
    if user_answer == 'N':
        print('Reboot the router and try to connect.')
        user_answer = input('Did that fix the problem? ')

if user_answer == 'Y' or user_answer == 'N':
    if user_answer == 'N':
        print('Make sure the cables between the router\nand modem are plugged in firmly.')
        user_answer = input('Did that fix the problem? ')

if user_answer == 'Y' or user_answer == 'N':
    if user_answer == 'N':
        print('Move the router to a new location.')
        user_answer = input('Did that fix the problem? ')
        
if user_answer == 'Y' or user_answer == 'N':
    if user_answer == 'N':
        print('Get a new router.')
                    
        


