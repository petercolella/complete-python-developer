username = input('What is your userame?')
password = input('What is your password?')
password_length = len(password)
masked_password = '*' * password_length

print(f'{username}, your password, {masked_password}, is {password_length} letters long.')