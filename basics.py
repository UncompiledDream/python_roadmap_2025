import random

def calculate_bmi(weight,height):
    bmi = weight/pow(height,2)
    return bmi

weight = 120#int(input("ВЕС:"))
height = 192#int(input("РОСТ:"))
if isinstance(weight,int) and isinstance(height,int):
    print(calculate_bmi(weight,height))
else:
    print("нужно ввести цифры")

def temperatyra(F):
    cel = ((f - 32) * 5/9)
    return cel
f = 5 #int(input("температура по фаренгейту"))
print(temperatyra(f))

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0 ]

numbers = []
for i in range(random.randint(15,25)):
    numbers.append(random.randint(5,100))

print(filter_even(numbers))

password = input("введите пароль")
print(password)
while password != "":
    password = input("введите правильный пароль")

def add_tax(price,tax_rate=0.13):
    return price * (1 + tax_rate)

print(round(add_tax(price=(random.randint(100,5000))),))


def generate_lottery_numbers():
    return sorted(random.sample(range(1,50),6))

print(generate_lottery_numbers())