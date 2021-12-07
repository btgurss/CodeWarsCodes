# Determining if a number is a narcissistic number - a number that is the sum of its own digits, each raised
# to the power of the number of digits in a given base.  Base 10 is used.

def narcissistic(value):
    # Setting counter to count digits and to use as exponent
    count = 0
    # Setting each digit to another integer (Creating array to hold all digits)
    x = [int(a) for a in str(value)]
    # Loop to count digits in array
    for number in x:
        count = count + 1
    # Declaring variable to hold sum
    nar = 0
    # Loop to find exponents and add to current values
    for digit in x:
        nar = digit ** count + nar

    # If statement to return whether number is narcissistic or not (True or False)
    if nar == value:
        return True
    else:
        return False
test = 122
print(narcissistic(test))