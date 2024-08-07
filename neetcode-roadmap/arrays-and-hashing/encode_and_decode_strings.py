def encode(strs):
    res = ''
    for s in strs:
        l = len(s)
        res = res + str(l) + '#' + s
    return res


def decode(s: str):
    res = []

    i = 0
    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1
        length = int(s[i:j])

        i = j + 1
        j = i + length

        res.append(s[i:j])

        i = j

    return res


print(encode(["neet", "code", "love", "you"]))
print(decode('4#neet4#code4#love3#you'))
