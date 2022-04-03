


def to_usd(my_price):

    """
    This function will format a number that is passed into the function as USD
    It will be comma separated and formatted as $0.00

    Invoke like this: to_usd(9.99999)
    """


    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":
    num = input("Choose a price like 4.87: ")
    print(to_usd(float(num)))


