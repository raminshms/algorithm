from collections import defaultdict


def groupAnagrams(strs):
    hm = defaultdict(list)

    for str in strs:
        count = [0] * 26

        for c in str:
            count[ord(c) - ord("a")] += 1

        hm[tuple(count)].append(str)

    return list(hm.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
