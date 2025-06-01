
# 1. Second Largest Number (Efficient)
def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

# 2. Palindrome Check (Two-pointer, memory efficient)
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

# 3. Character Frequency Count (Using dict)
def char_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 4. Merge Two Lists Without Duplicates (Preserve Order)
def merge_unique(l1, l2):
    seen = set(l1)
    result = l1[:]
    for item in l2:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage:
if __name__ == "__main__":
    print("Second Largest:", second_largest([4, 1, 9, 7, 9]))
    print("Is Palindrome:", is_palindrome("madam"))
    print("Char Frequency:", char_freq("banana"))
    print("Merged List:", merge_unique([1, 2, 3], [3, 4, 5]))
