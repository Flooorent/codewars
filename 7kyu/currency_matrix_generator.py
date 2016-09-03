#!/usr/bin/python

def generate_currency_matrix(currency):
    currencies = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    index = currencies.index(currency)
    matrix = []
    for i in range(len(currencies)):
        if i < index:
            matrix.append(currencies[i] + currency)
        elif i > index:
            matrix.append(currency + currencies[i])
    return matrix


# more beautiful with enumerate
def generate_currency_matrix(currency):
    currencies = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    index = currencies.index(currency)
    matrix = []
    for i, curr in enumerate(currencies):
        if i < index:
            matrix.append(curr + currency)
        elif i > index:
            matrix.append(currency + curr)
    return matrix

