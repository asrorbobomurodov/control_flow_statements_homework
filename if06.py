def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    pos_num = 0
    neg_num = 0
    
    if a>0:
        pos_num += 1
    if a<0:
        neg_num += 1

    if b>0:
        pos_num += 1
    if b<0:
        neg_num += 1

    if c>0:
        pos_num += 1
    if c<0:
        neg_num += 1

    if pos_num > neg_num:
        return "There are a lot of positive number"
    if neg_num > pos_num:
        return "There are a lot of negative number"

print(main(5,6,-10))
print(main(-3,-5,1))
print(main(7,0,-3))

