# When given a string of letters, this function will return the error rate for a color coding
# The error rate is number of letters not between a and m to total letters in string

def printer_error(s):
    # Variable numerator (bad letters)
    num = 0
    # Variable denominator (total letters)
    den = 0

    # Looping through each letter in string
    for letter in s:
        # Using if statement to check each letter
        if letter == "a" or letter == "b" or letter == "c" or letter == "d" or letter == "e" or letter == "f" or letter == "g" or letter == "h" or letter == "i" or letter == "j" or letter == "k" or letter == "l" or letter == "m":
            # Adding to the numerator if letter is listed above
            num += 1
        # Adding to denominator 
        den += 1
    # Writing answer as ratio using f string
    ratio = f"{num}/{den}"
    return(ratio)

test = "abamdingkdhhhkilllembcnquz"
printer_error(test)