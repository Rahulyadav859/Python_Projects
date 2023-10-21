email= input('Enter your email: ')

user_name = email[:email.index('@')]
domail_name = email[email.index('@')+1:]

print(f"Your user name is '{user_name}' and your domain is '{domail_name}'")
