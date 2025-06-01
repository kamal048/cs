l = [4, 1, 9, 7, 9]

first = second = float('-inf')

for num in l:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second)  # Output: 7