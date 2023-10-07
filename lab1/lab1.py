##########
# Q2
##########
print("Hello World")


##########
# Q3.1
##########
person1_name = input("Enter a person's name: ")
person1_age = int(input("Enter their age: "))

person2_name = input("Enter a person's name: ")
person2_age = int(input("Enter their age: "))

if person2_age > person1_age:
    print(f'{person2_name} is {person2_age - person1_age} years older than {person1_name}')
elif person2_age < person1_age:
    print(f'{person1_name} is {person1_age - person2_age} years older than {person2_name}')
else:
    print(f'{person1_name} and {person2_name} are the same age')


##########
# Q3.2
##########
total_sum = 0
is_negative = False

while not is_negative:
    new_num = float(input("Enter a number: "))
    if new_num < 0:
        is_negative = True
    else:
        total_sum += new_num

print(total_sum)


##########
# Q3.3
##########
amount = int(input("How many numbers would you like to enter? "))
numbers = []

for i in range(amount):
    num = float(input("Enter your number: "))
    numbers.append(num)

for i in range(amount - 1, -1, -1):
    print(numbers[i])