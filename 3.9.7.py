string = input("Введите числа через пробел:")

list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)