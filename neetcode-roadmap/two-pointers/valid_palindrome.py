def isPalindrome(s: str):
    str = ''
    for c in s:
        if c.isalnum():
            str += c.lower()

    start = 0
    end = len(str) - 1

    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1

    return True


print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
