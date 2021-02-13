from datetime import date
current_year = date.today().year

birth_year = input('What year were you born?')
age = current_year - int(birth_year)

print(f'You were born in {birth_year} and you\'re {age} years old')