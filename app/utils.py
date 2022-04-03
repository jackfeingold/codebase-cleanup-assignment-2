


def to_usd(my_price):

    """
    This function will format a number that is passed into the function as USD
    It will be comma separated and formatted as $0.00

    Invoke like this: to_usd(9.99999)
    """


    return '${:,.2f}'.format(my_price)