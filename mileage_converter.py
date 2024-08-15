CONVERSION_FACTOR = 0.621371

km = input('How many kilometers did you run today?\n')
mi = round(CONVERSION_FACTOR * float(km), 2)

msg = f'Your {km}km run was {mi}mi'
print(msg)