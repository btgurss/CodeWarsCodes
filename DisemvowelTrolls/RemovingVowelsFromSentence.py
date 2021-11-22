# Function to remove vowels from sentence or paragraph
def disemvowel(string_):

    # Setting string equal to nothing
    newString = ""

    # Looping through characters in sentence
    for char in string_:

        # Using if statement to check for vowels
        if (char != "a" and char != "e"and char != "i" and char != "o" and char != "u" and char != "A" and char != "E" and char != "I" and char != "O" and char != "U"):

            #Adding consonants to new string
            newString = newString + char
    return newString

# Test Set
test = "This website is for losers LOL!"
disemvowel(test)