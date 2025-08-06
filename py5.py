#Say you have a list value like this:

#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted 
#before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function 
#should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

#takes a list and puts all the values into a string with ', ' 
def toPrint(spam):
    length = len(spam)
    if length == 0:
        return 'List cannot be empty'
    elif length == 1:
        return spam[0]

    elif length == 2:
        return spam[0] + ' and ' + spam[1]

    else:
        result = ''
        for i in range(length-1):
            result += spam[i]
            result += ', '
        result += 'and '
        result += spam[-1]
        return result


spam = ['apples', 'bananas', 'tofu', 'cats']
print(toPrint(spam))

groceries = ['apples', 'grapes', 'pesto', 'pasta', 'butter', 'peanut butter']
print(toPrint(groceries))

supplies = ['pencils', 'scissors']
print(toPrint(supplies))

empty = []
print(toPrint(empty))

#needs error exception