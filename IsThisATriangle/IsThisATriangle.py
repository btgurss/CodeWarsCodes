# Given side lengths, determine if they could form a triangle

def is_triangle(a, b, c):
    
    # If statement to determine if each pair of sides sums to more than the third
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
