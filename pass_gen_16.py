import random, string

def passgen():
    length = 8
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for x in range(length))
    return password

print(passgen())
