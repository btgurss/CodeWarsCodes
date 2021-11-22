# Filter integers from a list of integers and strings
def filter_list(l):

    # Declaring array
    intList = []

    # Looping through parts of array
    for part in l:

        # Adding numbers to new array using if statement
        if type(part) is int:
            intList.append(part)
    print(intList)
    return intList


# Test Set
example = [1, 5, "Hello", 8, "Nice"]
filter_list(example)