# Finding the largest sum of non-consecutive integers
def LargestSumNonConsecutive(n):
    
    # Setting largest sum variable to zero
    LargestSum = 0

    #Setting counter to 0.  This will be used to count number of numbers in array
    count = 0

    #Looping through array to find count and to determine largest number for an exception case
    for number in n:
        count += 1
        if number > LargestSum:
            LargestSum = number
    
    # Setting a new counting variable to zero
    newCount = 0

    # Using while loop to go through numbers of array (stopping at 2 from the end)
    while newCount <= count - 3:
        # Counter to loop through second numbers of addition problem - starting this one +2 to from newCount variable to start 2 away from other counter
        count2 = newCount + 2

        # Looping through second numbers and checking to see if sum is larger than previous amount
        while count2 <= count - 1:
            if n[newCount] + n[count2] > LargestSum:
                LargestSum = n[newCount] + n[count2]
            # Increasing count of second checked number
            count2 += 1
        # Increasing count of first checked number
        newCount += 1
    
    print(LargestSum)


# Test Sets
test = [3, 5, 6, 3, 8, 13]
test1 = [5, 6, 5]
test2 = [4, 12, 5]
LargestSumNonConsecutive(test)
LargestSumNonConsecutive(test1)
LargestSumNonConsecutive(test2)