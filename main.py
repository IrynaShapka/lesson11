# def prime_generator(end):
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     current = 2
#     while current <= end:
#         if is_prime(current):
#             yield current
#         current += 1
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')


# import types
#
# from inspect import isgenerator
#
#
# def generate_cube_numbers(end) -> list[int]:
#     current = 2
#     cubes = []
#     while True:
#         cube = current ** 3
#         if cube <= end:
#             yield cube
#         else:
#             break
#         current += 1
#     return cubes
#
#
# gen = generate_cube_numbers(1)
#
# assert isgenerator(gen) == True, 'Test0'
#
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('Ok')


def is_even(number):
    last_digit = number % 10
    return last_digit in [0, 2, 4, 6, 8]


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
