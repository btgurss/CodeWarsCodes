# Function to count number of vowels in a sentence or phrase
def get_count(sentence):

    # Setting counter to zero
    counter = 0

    # Looping through characters of sentence
    for char in sentence:

        # Checking vowels with if statement
        if (char == "a" or char == "e"or char == "i" or char == "o" or char == "u"):
            counter += 1
    return counter

# Test Set
sentence = "Hello, How are you?"
print(get_count(sentence))