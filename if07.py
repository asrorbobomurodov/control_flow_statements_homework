def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==1:
        return "positive odd number"
    if a>0 and a%2==0:
        return "positive even number"
    if a<0 and a%2==1:
        return "negative odd number"
    if a<0 and a%1==0:
        return "negative even number"
    return "the number is zero"
print(main(4))
print(main(-9))
print(main(0))