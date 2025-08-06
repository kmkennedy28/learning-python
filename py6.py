
#takes a list and returns one string listing the items
def toPrint(spam):
    #list length
    length = len(spam)

    #cannot list an empty list
    if length == 0:
        return 'List cannot be empty'
    
    #if one item just return the item
    elif length == 1:
        return spam[0]

    #if two items return them without the comma
    elif length == 2:
        return spam[0] + ' and ' + spam[1]

    #if more than two items return them in a string divided by ', '
    else:
        result = ''
        for i in range(length-1):
            result += spam[i]
            result += ', '
        result += 'and '
        result += spam[-1]
        return result

#test printing a multi item string
spam = ['apples', 'bananas', 'tofu', 'cats']
print(toPrint(spam))

#test printing a long list
groceries = ['apples', 'grapes', 'pesto', 'pasta', 'butter', 'peanut butter']
print(toPrint(groceries))

#test printing a two item list
supplies = ['pencils', 'scissors']
print(toPrint(supplies))

# test printing a one item list
count = [1]
print(toPrint(count))

#test printing an empty list
empty = []
print(toPrint(empty))
