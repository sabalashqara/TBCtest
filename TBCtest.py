# code 1
print("Hello TBC")

# code 2 
for num in range(2, 10001, 2):
    print(num)

# code 3
def is_divisible_by_seven(number):
    return number % 7 == 0
print(is_divisible_by_seven(1), is_divisible_by_seven(7))

# code 4
import random

def is_sum_even():
    numbers = [random.randint(1, 100) for _ in range(10)]
    total = sum(numbers)
    print (numbers)
    print (total)
    print (total % 2 == 0)
is_sum_even() 

# code 5
import random

def generate_random_numbers():
    odd_numbers = []
    even_numbers = []
    
    while len(odd_numbers) < 10:
        num = random.randint(1, 100)
        if num % 2 != 0:
            odd_numbers.append(num)
    
    while len(even_numbers) < 10:
        num = random.randint(1, 100)
        if num % 2 == 0:
            even_numbers.append(num)

    return odd_numbers, even_numbers

def compare_sums():
    odd_numbers, even_numbers = generate_random_numbers()
    print (odd_numbers, even_numbers)
    sum_odd = sum(odd_numbers)
    sum_even = sum(even_numbers) 
    print (sum_odd, sum_even)      
    if sum_even > sum_odd and sum_even < 700:

        return True
    else:
        return False
print (compare_sums())

# code 6
def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
print(calculate_triangle_area(5, 4, 3))

# code 7 
import random

def greater_than_seven(number):
    return number > 7

random_number = random.randint(1, 20)
result = greater_than_seven(random_number)
print(random_number)
print(greater_than_seven(random_number))

# code 8 
import random

def generate_nums(min_val, max_val):
    return sum([num for num in range(min_val, max_val, 1) if num %3 == 0])
print(generate_nums(4, 17))