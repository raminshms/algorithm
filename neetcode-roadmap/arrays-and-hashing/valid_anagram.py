def isAnagram(s, t):
    if len(s) != len(t):
        return False

    sCounter = {}

    for c in s:
        sCounter[c] = sCounter.get(c, 0) + 1

    for ch in t:
        if ch not in sCounter or sCounter[ch] == 0:
            return False
        sCounter[ch] -= 1

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
