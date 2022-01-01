import string
import random

character_list = list(string.ascii_letters + string.digits + "!@#$%^&*()<>?/|:;{}[]+=")


def generate_random_password():
    length_of_password = int(input("\nPlease enter the desired length of the password : "))
    random.shuffle(character_list)
    password = []
    for i in range(length_of_password):
        password.append(random.choice(character_list))
    random.shuffle(password)
    print("".join(password))


generate_random_password()
