def dec_to_binary(x):
    digits = []
    while x > 0:
        a = x
        x = int(x / 2)
        e = (a - x * 2)
        digits.append(e)
    binary = ''.join(map(str, reversed(digits)))
    result = int(binary)
    print(result)
dec_to_binary(100)