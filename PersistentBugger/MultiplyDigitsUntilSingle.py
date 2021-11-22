# Function to find the number of times needed to multiply all digits of a number until that number becomes a single digit
def persistence(n):

    # Setting counter to determine the number of times the digits have been multiplied 
    count = 0

    # Looping through until the product is less than 9
    while n > 9:

        # Setting each digit to another integer (Creating array to hold all digits)
        x = [int(a) for a in str(n)]

        # Setting product to 1
        product = 1

        # Loop to multiply digits together
        for number in x:
            #Setting new product
            product = product * number
        n = product
        #Counting
        count += 1
        print(product)
    print(f"It took {count} times to get to a single digit")
    return count

# Test set
test = 394
persistence(test)