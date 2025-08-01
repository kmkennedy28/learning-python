
#performs the collatz sequence on number
def collatz(number):
    #if the number is even print & return number integer divided by 2
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    #if number is odd return & print 3 * number + 1
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result, sep= ' ')
        return result

userNumber = 0 #the user input number

#input validation
while True:
    try:
        #get user number & store as userNumber 
        print("Enter an integer number: ")
        userNumber = int(input(''))
        break #valid input breaks the loop
    except ValueError:
        print('Please enter an integer value.')

#loop until collatz returns 1
while(userNumber != 1):
    #put userNumber in collatz 
    userNumber = collatz(userNumber)

