def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    s=0
    if a<0:
        s = s+1
    if b<0:
        s = s+1
    if c<0:
        s = s+1
    return s
print(main(15,6,0))
print(main(8,-3,-2))
