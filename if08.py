def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 9<a<100 or -100<a<-9:
        if a%2==1:
            return "two-digit odd number"
        if a%2==0:
            return "two-dgit even number"
        
    if 99<a<1000 or -1000<a<-99:
        if a%2==1:
            return "three-digit odd number"
        if a%2==0:
            return "three-digit even number" 

print(main(985))
print(main(-242))
print(main(56))
print(main(-69))