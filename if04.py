def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    s = 0

    if a>0:
        s += 1

    if b>0:
        s += 1
    
    if c>0:
        s += 1

    return s

print(main(5,6,7))
print(main(7,-5,-3))
print(main(0,0,0))