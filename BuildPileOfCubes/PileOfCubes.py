# Counting the number of times, when given an integer, that an increasing value of n^3 will sum to
# given integer.  A value of -1 is returned if exact sum is not reached.

def find_nb(m):
    # Using a placeholder variable so I do not change original
    placeholder = m
    # Using a counter
    counter = 0
    # Using a while loop to go through until number reaches zero
    while placeholder > 0:
        # Counting
        counter += 1
        # Subtracting a cubed amount from the previous number and resetting placeholder
        placeholder = placeholder - counter**3
        # Returning a -1 if value drops below zero
        if placeholder < 0:
            return (-1)
    return (counter)

test = 1071225
test2 = 91716553919377
print(find_nb(test2))