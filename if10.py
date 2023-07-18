def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        return "Freezing"
    if 0<temp<11:
        return "Very Cold"
    if 10<temp<21:
        return "Cold"
    if 20<temp<31:
        return "Normal"
    if 30<temp<41:
        return "Hot"
    if temp>40:
        return "Very hot"
print(main(-18))
print(main(0))
print(main(16))