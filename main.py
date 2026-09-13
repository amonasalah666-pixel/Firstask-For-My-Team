def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([4, 12, 7, 19, 3]))
print(find_largest([-4, -3, -7, -12]))
