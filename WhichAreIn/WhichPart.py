# Given two arrays of strings (a1, a2) we want to return a sorted array in lexicographical order of the
# strings of a1 which are substrings of strings a2
def in_array(array1, array2):
    
    #Declaring variable array
    subs = []

    # Using nested for loop to cycle through parts of each array
    for input in array1:
        for word in array2:

            #Adding parts of words to new arrays if they are found in second array
            if input in word and input not in subs:
                subs.append(input)
                
    #Sorting array lexicographically
    subs.sort()
    return(subs)

test = ["arp", "live", "strong"]
test2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(test, test2)