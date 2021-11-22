def count_bits(n):
    # Setting variable to product of a power
    power = 0
    # Initializing exponent counter
    exponent = 0
    #Using while loop to count up until 2 to the nth degree is larger than input number
    while power < n:
        #Setting power equal to 2 to the nth degree
        power = 2**exponent
        #Adding 1 to the exponent
        exponent += 1
    #Initializing the number of bits (ones in binary)
    bits = 0
    #Initializing a number to the input number
    reducedNumber = n
    #Initializing binary as an empty string
    binary = ""
    #Using while loop to count down exponents
    while exponent >= 0:
        #Counting down if n is smaller than 2 to the nth power
        if 2**exponent > n:
            #Subtracting 1 from exponent
            exponent=exponent-1
        #Determining if 2 to the exponent power is lower than input number (This number will change as the loop continues)
        elif 2**exponent <= reducedNumber:
            #Subtracting 2 to the nth degree from initial number and setting this amount to a reduced number
            reducedNumber = reducedNumber-2**exponent
            #Adding one to the bits
            bits += 1
            #Setting binary digit to 1
            binary = binary + "1"
            #Subtracting one from exponent
            exponent = exponent-1
            print(f"Binary: {binary}")
        #Going to else if number is 2 to nth power is greater than the reduced number
        else:
            #Setting binary equal to zero
            binary = binary + "0"
            #Subtracting one from exponent
            exponent = exponent-1
        print(f"The Reduced number is now: {reducedNumber}")
    print(f"The final number of bits is {bits}")
    print(f"The final binary code is {binary}")  
    return bits

#Using function
val = input ("Enter your number: ")
print(f"You chose the number: {val}")
print(count_bits(int(val)))
