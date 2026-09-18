def exchange_money(budget, exchange_rate):
    value = float(budget/exchange_rate)
    return value

def get_change(budget, exchanging_value):
    remainder = budget - exchanging_value
    return remainder


def get_value_of_bills(denomination, number_of_bills):
    total = denomination * number_of_bills
    return total
    

def get_number_of_bills(amount, denomination):
    number_of_bills = amount//denomination
    return number_of_bills


def get_leftover_of_bills(amount, denomination):
    answer = amount % denomination
    return answer


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread = spread/100
    exchange_rate = exchange_rate * (1+spread)
    value = budget/exchange_rate
    left = value % denomination
    value = (value - left)
    return value
    