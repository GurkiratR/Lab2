def print_list_numbers(numbers_list):
    for number in numbers_list:
        print(number)

def print_numbers_greater_than_5(numbers_list):
    for number in numbers_list:
        if number > 5:
            print(number)

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("All the numbers in the list:")
print_list_numbers(myNumbers)

print("\nList of numbers that are larger than 5:")
print_numbers_greater_than_5(myNumbers)
