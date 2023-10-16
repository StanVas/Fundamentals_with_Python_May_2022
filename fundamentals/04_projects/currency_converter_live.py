from forex_python.converter import CurrencyRates

amount = int(input('Enter the amount:'))
c = CurrencyRates()
current_rate = c.get_rate("GBP", "USD")
result = current_rate * amount
print(f'Your sum in dollars is: {result:.2f}')
