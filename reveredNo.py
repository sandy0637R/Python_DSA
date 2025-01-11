num = 12345

reversed_num = 0
is_negative = num < 0

if is_negative:
    num = -num

while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num //= 10

if is_negative:
    reversed_num = -reversed_num

print(reversed_num)
