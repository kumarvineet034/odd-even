def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Sample list of numbers
numbers = [12, 7, 18, 5, 23, 6, 9, 10, 17]

even_count, odd_count = count_even_odd(numbers)

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)