# Function similar to fibonacci sequence except with 3 numbers instead of 2
def tribonacci(signature, n):
    
    # Using if/else statements to check exceptions
    if n==0:
        signature = []
    elif n==1:
        signature = [1]
    else:
        # Looping through numbers in array and adding numbers on
        for i in range (0,n-3):
            sum = signature[i] + signature[i + 1] + signature[i + 2]
            signature.append(sum)
    
test = [3, 2, 1]
test1 = 0
tribonacci(test, test1)