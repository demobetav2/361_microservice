import subprocess



base_currency = 'USD'
target_currency = 'CAD'
value = 100

get_rate = subprocess.run(['python', 'exchangeRate.py', base_currency, target_currency],
                       capture_output=True,
                       text=True)




response = get_rate.stdout
conversion_rate = get_rate.stdout.split()

# If first element in string is 'success', valid conversion received, perform calculation
if conversion_rate[0] == 'success':

    print(f'Your {value} in {base_currency} is currently worth {float(conversion_rate[1]) * value} in {target_currency}.')

# Unsuccessful request, process error response
else:
    pass
