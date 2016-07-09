# Numbers

number = 1 + 2 * 3 / 4.0
print number

brackets = (1 + 2) * 3 / 4.0
print brackets

remainder = 11 % 3
print remainder

power = 5 ** 3
print power


# Strings

andromeda = "Andromeda"
print andromeda + " loves her treats."
print andromeda * 15

andromeda15 = andromeda * 15
print andromeda15


# Lists

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
all_numbers.sort()
print all_numbers + sorted(all_numbers, reverse=True) + all_numbers
