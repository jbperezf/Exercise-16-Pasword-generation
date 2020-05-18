import random
import string


def generate_password(password_length=16, characters=string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.sample(characters, password_length))


custom_length = int(input("How many characters should the password have?: "))
print(generate_password(custom_length))
