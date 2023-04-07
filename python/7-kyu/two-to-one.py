def longest(a1, a2):
    # your code
    a3 = "".join(set(a1+a2))
    output = "".join(sorted(a3))
    return output
