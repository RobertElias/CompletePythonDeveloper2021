

print(type(int(str(100))))
print(int("0b100",2))
print(bin(5))


first_name = input("What is your name? ")
birth_year = input('what year were you born? ')


age = 2019 - int(birth_year)


print(f'Hello {first_name}, your age is: {age}')
