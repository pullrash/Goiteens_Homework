def simple_num(num):
    if num <= 3:
        return True
    else:
        for i in range(1, num-1):
            if num % (num-i) == 0:
                return False
        return True

def simple_nums_generator():
    num = 1
    while True:
        if simple_num(num):
            yield num
        num += 1 


generator1 = simple_nums_generator()

for _ in range(10):
    print(next(generator1))

print()
import random

existing_password = []
LETTER_AND_DIGIT = "qwertyuiopasdfghjkzxcvbnm1234567890"
def create_password():
    parts = []
    for _ in range(4):
        parts.append(random.choice(LETTER_AND_DIGIT))
    return parts[0] + parts[1] + parts[2] + parts[3]

def generate_password():
    while True:
        password = ""
        for _ in range(4):
            password = create_password()
        if password not in existing_password:
            yield password
            existing_password.append(password)

generator2 = generate_password()
for _ in range(100):
    print(next(generator2), end=" ")